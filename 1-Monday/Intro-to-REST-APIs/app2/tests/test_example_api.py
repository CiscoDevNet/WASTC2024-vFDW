import pytest
from app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello(client):
    rv = client.get("/api/hello")
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data == {"message": "Hello, world!"}
