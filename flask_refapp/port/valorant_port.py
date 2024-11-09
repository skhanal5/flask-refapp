import abc
from abc import ABC


class ValorantPort(ABC):
    @abc.abstractmethod
    def get_player_overview(self, team: str):
        pass

    @abc.abstractmethod
    def get_team_overview(self, team: str):
        pass

    @abc.abstractmethod
    def get_all_teams_in_region(self, team: str):
        pass

    @abc.abstractmethod
    def get_match_details(self, team: str):
        pass

    @abc.abstractmethod
    def get_upcoming_matches(self, team: str):
        pass

    @abc.abstractmethod
    def get_previous_results(self, team: str):
        pass
