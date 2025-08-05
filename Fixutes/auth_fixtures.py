import pytest
from api_handler.request_handler import RequestHandler

@pytest.fixture(scope="session")
def api_client():
    return RequestHandler(base_url="https://fakestoreapi.in/api")

@pytest.fixture(scope="session")
def auth_token(api_client):
    response = api_client.post("/auth/login", json={"username": "user", "password": "pass"})
    return response.json()["token"]
