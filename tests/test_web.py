from olympics.web import app

def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Interface Web Olympics" in response.data


def test_top_discipline_valid():
    client = app.test_client()
    response = client.get("/discipline/3?top=5")
    assert response.status_code == 200
    # Vérifie que le tableau s'affiche
    assert b"<table" in response.data


def test_top_discipline_invalid_type():
    client = app.test_client()
    response = client.get("/discipline/abc")
    # Flask renvoie 404 car abc n'est pas un <int>
    assert response.status_code == 404
