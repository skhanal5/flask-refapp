from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
from flask.testing import FlaskClient

from vleague_backend.routes.valorant_route import get_port


class TestValorant:
    @pytest.fixture(scope="module")
    def mock_adapter(self) -> MagicMock:
        mock_adapter = MagicMock()
        mock_adapter.get_health.return_value = {}
        mock_adapter.get_team.return_value = {}
        mock_adapter.get_upcoming_matches.return_value = []
        mock_adapter.get_previous_results.return_value = []
        mock_adapter.get_player.return_value = {}
        mock_adapter.get_all_teams = {}
        return mock_adapter

    @pytest.fixture(scope="module")
    def mock_port(self, mock_adapter):
        with patch("vleague_backend.routes.valorant_route.VLRAdapter") as mock_module:
            mock_module.return_value = mock_adapter
            yield mock_adapter

    def test_get_port(self, mock_port: Generator[MagicMock, None, None]):
        result = get_port()
        assert result == mock_port

        # invoke once more
        result = get_port()
        assert result == mock_port

    def test_get_health(self, client: FlaskClient, mock_port: MagicMock):
        response = client.get("/valorant/health")
        assert response.status_code == 200
        assert response.json == {}
        mock_port.get_health.assert_called_once()

    def test_get_team_happy(self, client: FlaskClient, mock_port: MagicMock):
        response = client.get("/valorant/teams/foo")
        assert response.status_code == 200
        assert response.json == {}
        mock_port.get_team.assert_called_with("foo")

    def test_get_upcoming_matches_happy(
        self, client: FlaskClient, mock_port: MagicMock
    ):
        response = client.get("/valorant/teams/foo/matches")
        assert response.status_code == 200
        assert response.json == []
        mock_port.get_upcoming_matches.assert_called_with("foo")

    def test_get_team_results_happy(self, client: FlaskClient, mock_port: MagicMock):
        response = client.get("/valorant/teams/foo/results")
        assert response.status_code == 200
        assert response.json == []
        mock_port.get_previous_results.assert_called_with("foo")

    def test_get_teams_happy(self, client: FlaskClient, mock_port: MagicMock):
        response = client.get("/valorant/teams")
        assert response.status_code == 200
        assert response.json == {}

    def test_get_player_happy(self, client: FlaskClient, mock_port: MagicMock):
        response = client.get("/valorant/players/foo")
        assert response.status_code == 200
        assert response.json == {}
        mock_port.get_player.assert_called_with("foo")
