from sqlalchemy.orm import Session
from sqlalchemy import func
from olympics.database import SessionLocal
from olympics.database import Medal, Country, Athlete, Team, Event


def get_top_countries_by_discipline_orm(discipline_id: int, top: int = 5):
    session = SessionLocal()

    # COALESCE version ORM : on construit le champ country_id
    country_id_expr = func.coalesce(Athlete.country_id, Team.country_id)

    results = (
        session.query(
            Country.name.label("country"),
            func.count(Medal.id).label("medals")
        )
        .join(Event, Medal.event_id == Event.id)
        .outerjoin(Athlete, Medal.athlete_id == Athlete.id)
        .outerjoin(Team, Medal.team_id == Team.id)
        .join(Country, Country.id == country_id_expr)
        .filter(Event.discipline_id == discipline_id)
        .group_by(Country.name)
        .order_by(func.count(Medal.id).desc())
        .limit(top)
        .all()
    )

    session.close()
    return results
