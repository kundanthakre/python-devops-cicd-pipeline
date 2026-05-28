from app import app   # IMPORTANT: import Flask instance, not module

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
