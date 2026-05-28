import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app

def test_home():
    client = flask_app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_health():
    client = flask_app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
