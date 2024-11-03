from unittest.mock import MagicMock, patch

import pytest
from flask.testing import FlaskClient


@pytest.fixture()
def mock_service() -> MagicMock:
    with patch(
        "flask_refapp.services.valorant_service.ValorantService.get_health"
    ) as mock_method:
        mock_method.return_value = {"status": "healthy"}
        yield mock_method


def test_get_health(client: FlaskClient, mock_service: MagicMock):
    response = client.get("/valorant/health")
    assert response.status_code == 200
    mock_service.assert_called_once()
