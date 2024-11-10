from httpx import Client, Request, Response
from typing import Any


class HTTPClient:
    def __init__(self, base_url: str):
        self._client = Client(base_url=base_url)

    def send_request(
        self,
        method: str,
        headers: dict[str, Any],
        base_url: str,
        params: dict[str, Any] | None = None,
    ) -> Response:
        request = self.__make_request(method, headers, base_url, params)
        return self._client.send(request)

    def __make_request(
        self,
        method: str,
        headers: dict[str, Any],
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> Request:
        return self._client.build_request(
            method=method, headers=headers, url=endpoint, params=params
        )

    def close(self):
        self._client.close()
