from typing import Any

from pydantic import BaseModel


class GeneralTeamData(BaseModel):
    id: str
    url: str
    name: str
    img: str
    country: str


class AllTeamsResponse(BaseModel):
    status: str
    region: str
    size: int
    pagination: dict[str, Any]
    data: list[GeneralTeamData]


class TeamPlayer(BaseModel):
    id: str
    url: str
    user: str
    name: str
    img: str
    country: str


class TeamStaff(BaseModel):
    id: str
    url: str
    user: str
    name: str
    tag: str
    img: str
    country: str


class TeamEvent(BaseModel):
    id: str
    url: str
    name: str
    results: list[str]
    year: str


class Match(BaseModel):
    id: str
    url: str


class Event(BaseModel):
    name: str
    logo: str


class MatchTeams(BaseModel):
    name: str
    tag: str
    logo: str
    points: str


class PreviousResults(BaseModel):
    match: Match
    event: Event
    teams: list[MatchTeams]


class UpcomingMatches(BaseModel):
    match: Match
    event: Event
    team: list[MatchTeams]


class DetailedEvents(BaseModel):
    id: str
    url: str
    name: str
    results: list[str]
    year: str


class DetailedTeamData(BaseModel):
    info: dict[str, str]
    players: list[TeamPlayer]
    staff: list[TeamStaff]
    inactive: list[Any] = []
    events: list[DetailedEvents]
    results: list[PreviousResults]
    upcoming: list[UpcomingMatches] = []


class DetailedTeamResponse(BaseModel):
    status: str
    data: DetailedTeamData
