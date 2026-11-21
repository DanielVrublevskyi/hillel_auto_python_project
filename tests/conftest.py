import pytest

from core.api_client import ApiClient
from api.auth_api import AuthApi
from config.settings import API_BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD

@pytest.fixture
def api_client():
    client = ApiClient(API_BASE_URL)

    yield client

    client.session.close()


@pytest.fixture
def auth_api(api_client):
    return AuthApi(api_client)

@pytest.fixture
def authenticated_client(auth_api, api_client):
    if not TEST_USER_EMAIL or not TEST_USER_PASSWORD:
        raise ValueError("Test user credentials are not configured")
    user_data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD
    }
    response = auth_api.signin(user_data)
    assert response.status_code == 200

    return api_client