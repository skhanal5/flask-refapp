from functools import lru_cache
from typing import Any

from flask import Blueprint
from flask_pydantic import validate

from vleague_backend.adapters.vlr_adapter import VLRAdapter
from vleague_backend.models.vlr_orl import PreviousResults, UpcomingMatches
from vleague_backend.port.valorant_port import ValorantPort

valorant_bp = Blueprint("valorant", __name__, url_prefix="/valorant")


@lru_cache
def get_port() -> ValorantPort:
    return VLRAdapter()


@valorant_bp.route("/health")
def get_health() -> dict[str, Any]:
    port = get_port()
    return port.get_health()


@valorant_bp.route("/teams/<team_name>")
@validate()
def get_team(team_name: str) -> dict[str, Any]:
    port = get_port()
    return port.get_team(team_name)


@valorant_bp.route("/teams/<team_name>/matches")
@validate()
def get_upcoming_matches(team_name: str) -> list[UpcomingMatches]:
    port = get_port()
    return port.get_upcoming_matches(team_name)


@valorant_bp.route("/teams/<team_name>/results")
@validate()
def get_team_results(team_name: str) -> list[PreviousResults]:
    port = get_port()
    return port.get_previous_results(team_name)


@valorant_bp.route("/players/<player_name>")
@validate()
def get_player(player_name: str) -> dict[str, Any]:
    port = get_port()
    return port.get_player(player_name)


@valorant_bp.route("/teams")
def get_teams() -> dict[str, Any]:
    port = get_port()
    return port.get_all_teams
