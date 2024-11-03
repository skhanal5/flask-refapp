from httpx import Response

from flask_refapp.clients.http_client import HTTPClient
from flask_refapp.clients.request import Request


class VLRAdapter:
    base_url = "https://vlrggapi.vercel.app"

    def __init__(self, client: HTTPClient = None):
        self._client = client or HTTPClient(base_url=VLRAdapter.base_url)
        self._default_headers = {"Content-Type": "application/json"}

    def get_health_status(self) -> Response:
        return self._client.send_request(
            method=Request.GET, headers=self._default_headers, endpoint="/health"
        )
