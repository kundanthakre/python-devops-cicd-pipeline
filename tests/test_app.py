import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def test_home():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_health():
    client = app.app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
