from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

def test_top_countries_by_discipline():
    rows = db.get_top_countries_by_discipline(3, 5)
    assert len(rows) <= 5
