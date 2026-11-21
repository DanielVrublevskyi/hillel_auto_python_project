import logging
import requests

logger = logging.getLogger(__name__)

class ApiClient:

    def __init__(self, base_url: str, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        # Create an HTTP session to manage cookies and connections
        self.session = requests.Session()
        self.timeout = timeout

    def send_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        response = self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs)
        logger.info(f"{response.request.method}: {response.request.url}")
        logger.info(f"Response status: {response.status_code}")
        return response
