from faker import Faker

from api.users_api import UsersApi
from api.auth_api import AuthApi
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestAuth:

    def test_post_signup(self, auth_api):
        fake = Faker("en_US")
        name = fake.first_name()
        last_name = fake.last_name()
        email = f"test_{fake.uuid4()[:12]}@example.com"
        password = fake.password(length=12, special_chars=False)

        user_data = {
            "name": name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "repeatPassword": password
        }
        response = auth_api.signup(user_data)
        assert response.status_code == 201

    def test_post_signin(self, auth_api):
        user_data = {
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD
        }
        response = auth_api.signin(user_data)
        assert response.status_code == 200

    def test_get_logout(self, authenticated_client):
        auth_api = AuthApi(authenticated_client)
        response = auth_api.logout()
        assert response.status_code == 200

        users_api = UsersApi(authenticated_client)
        response = users_api.get_current_user()
        assert response.status_code == 401

    def test_post_reset_password(self, auth_api):
        fake = Faker("en_US")
        name = fake.first_name()
        last_name = fake.last_name()
        email = f"test_{fake.uuid4()[:12]}@example.com"
        password = fake.password(length=12, special_chars=False)

        user_data = {
            "name": name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "repeatPassword": password
        }
        response = auth_api.signup(user_data)
        assert response.status_code == 201

        body_email = {"email": email}
        response = auth_api.reset_password(body_email)
        assert response.status_code == 200
        assert response.json().get("status") == "ok"



