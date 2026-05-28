```python id="g42v7v"
from app.app import app

def test_home():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
```
