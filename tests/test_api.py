from fastapi.testclient import TestClient

from olympics import api


client = TestClient(api.app)


def test_countries():
    response = client.get('/countries/')
    assert response.status_code == 200
    assert len(response.json()) > 100

def test_api_top_by_discipline():
    response = client.get('/top-by-discipline/?discipline_id=3&top=5')
    assert response.status_code == 200
    assert len(response.json()) <= 5

def test_api_invalid_discipline_type():
    response = client.get("/top-by-discipline/?discipline_id=abc&top=5")
    # FastAPI doit rejeter ce type
    assert response.status_code == 422
