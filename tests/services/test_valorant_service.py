from typing import Generator
from unittest.mock import MagicMock, patch

import pytest

from vleague_backend.adapters.vlr_adapter import VLRAdapter
from vleague_backend.services.valorant_service import ValorantService


@pytest.fixture()
def mock_adapter() -> Generator[MagicMock, None, None]:
    with patch(
        "flask_refapp.services.valorant_service.VLRAdapter.get_health_status"
    ) as mock_method:
        mock_method.return_value = {"status": "healthy"}
        yield mock_method


def test_service_initialization():
    service = ValorantService()
    assert service._adapter is not None
    assert isinstance(service._adapter, VLRAdapter)


def test_get_health(mock_adapter):
    service = ValorantService()
    result = service.get_health()
    assert result == {"status": "healthy"}
    mock_adapter.assert_called_once()
