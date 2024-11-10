from unittest.mock import patch

import pytest
from httpx import Client

from vleague_backend.clients.http_client import HTTPClient


@pytest.fixture()
def http_client() -> HTTPClient:
    client = HTTPClient("")
    return client


def test_client_initialization(http_client: HTTPClient):
    assert http_client._client is not None
    assert isinstance(http_client._client, Client)
    assert http_client._client.base_url == ""


def test_send_request(http_client: HTTPClient):
    with patch("httpx.Client.send") as mock_send:
        mock_send.return_value = {"key": "value"}
        result = http_client.send_request("GET", {}, "/foo")
        assert result == {"key": "value"}
