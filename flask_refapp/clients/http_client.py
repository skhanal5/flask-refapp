from httpx import Client, Request, Response


class HTTPClient:
    def __init__(self, base_url: str):
        self._client = Client(base_url=base_url)

    def send_request(
        self, method: str, headers: dict[str, any], endpoint: str
    ) -> Response:
        request = self.__make_request(method, headers, endpoint)
        return self._client.send(request)

    def __make_request(
        self, method: str, headers: dict[str, any], endpoint: str
    ) -> Request:
        return self._client.build_request(method=method, headers=headers, url=endpoint)

    def close(self):
        self._client.close()
