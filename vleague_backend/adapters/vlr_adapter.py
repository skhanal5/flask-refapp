from functools import cached_property
from typing import Any


from vleague_backend.clients.http_client import HTTPClient
from vleague_backend.clients.request import Request
from vleague_backend.models.vlr_gg import DetailedPlayerStats
from vleague_backend.models.vlr_orl import (
    AllTeamsResponse,
    DetailedTeamResponse,
)
from vleague_backend.port.valorant_port import ValorantPort


class VLRAdapter(ValorantPort):
    vlr_gg_api_base_url = "https://vlrggapi.vercel.app/"
    vlr_orl_base_url = "https://vlr.orlandomm.net/api/v1/"

    region = "na"  # hardcoded region for now
    default_headers = {"Content-Type": "application/json"}
    stats_endpoint = "stats"
    health_endpoint = "health"
    teams_endpoint = "teams"
    players_endpoint = "players"

    def __init__(self):
        self._client = HTTPClient(base_url="")

    def get_health(self) -> dict[str, Any]:
        full_url = VLRAdapter.get_full_url(
            base_url=self.vlr_gg_api_base_url, endpoint=self.health_endpoint
        )
        response = self._client.send_request(
            method=Request.GET, headers=self.default_headers, base_url=full_url
        )
        return response.json()

    @cached_property
    def get_all_player_stats(self) -> dict[str, Any]:
        full_url = VLRAdapter.get_full_url(
            base_url=self.vlr_gg_api_base_url, endpoint=self.stats_endpoint
        )
        response = self._client.send_request(
            method=Request.GET,
            headers=self.default_headers,
            base_url=full_url,
            params={"region": self.region, "timestamp": "30"},
        )
        return DetailedPlayerStats(**response.json()).model_dump()

    def get_player(self, player: str) -> dict[str, Any]:
        results = self.get_all_player_stats
        player_data = results.data.segments
        for individual_player in player_data:
            if player == individual_player.player:
                return individual_player
        raise Exception("Failed to get a response")

    # TODO: Expensive function, cache this result somehow
    def get_team(self, team: str) -> dict[str, Any]:
        result = self.get_all_teams
        team_id = VLRAdapter.get_team_id_from_teams(result, team)
        full_url = VLRAdapter.get_full_url(
            base_url=self.vlr_orl_base_url, endpoint=self.teams_endpoint
        )
        params = {"teamid": team_id}
        response = self._client.send_request(
            method=Request.GET,
            headers=self.default_headers,
            base_url=full_url,
            params=params,
        )
        print(f"Response: {response}")
        return DetailedTeamResponse(**response.json()).model_dump()

    @cached_property
    def get_all_teams(self) -> AllTeamsResponse:
        full_url = VLRAdapter.get_full_url(
            base_url=self.vlr_orl_base_url, endpoint=self.teams_endpoint
        )
        params = {"page": 1, "limit": "all", "region": self.region}
        response = self._client.send_request(
            method=Request.GET,
            headers=self.default_headers,
            base_url=full_url,
            params=params,
        )
        return AllTeamsResponse(**response.json())

    def get_upcoming_matches(self, team: str) -> list:
        team_data = self.get_team(team)
        return team_data["data"].upcoming

    def get_previous_results(self, team: str) -> list:
        team_data = self.get_team(team)
        return team_data["data"].results

    # TODO: Hash results {team_name => team}
    @staticmethod
    def get_team_id_from_teams(response: AllTeamsResponse, team: str) -> str:
        for team_data in response.data:
            if team_data.name == team:
                return team_data.id
        print(response)
        raise Exception("Failed to get a response")

    @staticmethod
    def get_full_url(base_url: str, endpoint: str) -> str:
        return f"{base_url}{endpoint}"
