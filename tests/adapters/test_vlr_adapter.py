from typing import Generator
from unittest.mock import patch, MagicMock

import pytest

from vleague_backend.adapters.valorant_adapter import VLRAdapter
from vleague_backend.clients.http_client import HTTPClient


@pytest.fixture()
def mock_client() -> Generator[MagicMock, None, None]:
    with patch(
        "flask_refapp.clients.http_client.HTTPClient.send_request"
    ) as mock_method:
        mock_method.return_value = {"status": "healthy"}
        yield mock_method


def test_adapter_initialization():
    adapter = VLRAdapter()
    assert adapter._client is not None
    assert isinstance(adapter._client, HTTPClient)
    assert adapter._default_headers == {"Content-Type": "application/json"}


def test_get_health_status(mock_client):
    adapter = VLRAdapter()
    result = adapter.get_health_status()
    assert result == {"status": "healthy"}
    mock_client.assert_called_once()
