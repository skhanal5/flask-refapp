from unittest.mock import patch, MagicMock

import pytest

from flask_refapp.adapters.vlr_adapter import VLRAdapter
from flask_refapp.clients.http_client import HTTPClient


@pytest.fixture()
def mock_client() -> MagicMock:
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
