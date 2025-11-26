from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

DATABASE_URL = "sqlite:///./database/olympics.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Athlete(Base):
    __tablename__ = "athlete"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country")

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country")

class Discipline(Base):
    __tablename__ = "discipline"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    discipline_id = Column(Integer, ForeignKey("discipline.id"))

    discipline = relationship("Discipline")

class Medal(Base):
    __tablename__ = "medal"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    date = Column(Date)
    athlete_id = Column(Integer, ForeignKey("athlete.id"))
    team_id = Column(Integer, ForeignKey("team.id"))
    event_id = Column(Integer, ForeignKey("event.id"))

    athlete = relationship("Athlete")
    team = relationship("Team")
    event = relationship("Event")