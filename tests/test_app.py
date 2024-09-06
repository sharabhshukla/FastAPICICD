from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "API Root, visit /docs for documentation related to the api"

def test_health_ping():
    response = client.get("/health-ping")
    assert response.status_code == 200
    assert response.text == "Ok"