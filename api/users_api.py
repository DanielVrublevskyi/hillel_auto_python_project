import requests

from core.api_client import ApiClient


class UsersApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def get_current_user(self) -> requests.Response:
        return self.client.send_request(
            method="GET",
            endpoint="/users/current")