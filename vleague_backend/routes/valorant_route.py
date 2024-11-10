from functools import lru_cache

from flask import Blueprint
from flask_pydantic import validate

from vleague_backend.adapters.valorant_adapter import VLRAdapter
from vleague_backend.port.valorant_port import ValorantPort

valorant_bp = Blueprint("valorant", __name__, url_prefix="/valorant")


@lru_cache
def get_port() -> ValorantPort:
    return VLRAdapter()


@valorant_bp.route("/health")
def get_health() -> dict:
    port = get_port()
    return port.get_health().json()


@valorant_bp.route("/teams/<team_name>")
@validate()
def get_team(team_name: str) -> dict:
    port = get_port()
    return port.get_team(team_name).model_dump()


@valorant_bp.route("/team/<team_name>/matches")
@validate()
def get_team_matches(team_name: str):
    port = get_port()
    return port.get_upcoming_matches(team_name)


@valorant_bp.route("/team/<team_name>/results")
@validate()
def get_team_results(team_name: str):
    port = get_port()
    return port.get_previous_results(team_name)


@valorant_bp.route("/players/<player_name>")
@validate()
def get_player(player_name: str):
    port = get_port()
    return port.get_player(player_name)


@valorant_bp.route("/teams")
def get_teams() -> dict:
    port = get_port()
    return port.get_all_teams.model_dump()
