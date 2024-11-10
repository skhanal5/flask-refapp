import abc
from abc import ABC
from functools import cached_property

from vleague_backend.models.vlr_gg import PlayerStat
from vleague_backend.models.vlr_orl import (
    DetailedTeamResponse,
    AllTeamsResponse,
    UpcomingMatches,
    PreviousResults,
)


class ValorantPort(ABC):
    @abc.abstractmethod
    def get_health(self):
        pass

    @abc.abstractmethod
    def get_player(self, player: str) -> PlayerStat:
        pass

    @abc.abstractmethod
    def get_team(self, team: str) -> DetailedTeamResponse:
        pass

    @abc.abstractmethod
    @cached_property
    def get_all_teams(self) -> AllTeamsResponse:
        pass

    @abc.abstractmethod
    def get_upcoming_matches(self, team: str) -> list[UpcomingMatches]:
        pass

    @abc.abstractmethod
    def get_previous_results(self, team: str) -> list[PreviousResults]:
        pass
