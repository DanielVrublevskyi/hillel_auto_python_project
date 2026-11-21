import requests

from core.api_client import ApiClient


class AuthApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def signup(self, user_data: dict) -> requests.Response:
        return self.client.send_request(
            method="POST",
            endpoint="/auth/signup",
            json=user_data)

    def signin(self, user_data: dict) -> requests.Response:
        return self.client.send_request(
            method="POST",
            endpoint="/auth/signin",
            json=user_data)

    def logout(self) -> requests.Response:
        return self.client.send_request(
            method="GET",
            endpoint="/auth/logout")

    def reset_password(self, email: dict) -> requests.Response:
        return self.client.send_request(
            method="POST",
            endpoint="/auth/resetPassword",
            json=email
        )