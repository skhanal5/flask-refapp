import abc
from abc import ABC
from functools import cached_property
from typing import Any

from vleague_backend.models.vlr_orl import (
    UpcomingMatches,
    PreviousResults,
)


class ValorantPort(ABC):
    @abc.abstractmethod
    def get_health(self) -> dict[str, Any]:
        pass

    @abc.abstractmethod
    def get_player(self, player: str) -> dict[str, Any]:
        pass

    @abc.abstractmethod
    def get_team(self, team: str) -> dict[str, Any]:
        pass

    @abc.abstractmethod
    @cached_property
    def get_all_teams(self) -> dict[str, Any]:
        pass

    @abc.abstractmethod
    def get_upcoming_matches(self, team: str) -> list[UpcomingMatches]:
        pass

    @abc.abstractmethod
    def get_previous_results(self, team: str) -> list[PreviousResults]:
        pass
