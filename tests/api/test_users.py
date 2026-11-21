from api.users_api import UsersApi
from models.users_models import CurrentUserResponse

class TestUsers:

    def test_get_current_user(self, authenticated_client):
        users_api = UsersApi(authenticated_client)
        response = users_api.get_current_user()

        assert response.status_code == 200
        user = CurrentUserResponse.model_validate(response.json(), strict=True)
        assert user.status == "ok"