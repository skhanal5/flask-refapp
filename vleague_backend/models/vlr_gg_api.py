from pydantic import BaseModel


class PlayerStat(BaseModel):
    player: str
    org: str
    agents: list[str]
    rounds_played: str
    rating: str
    average_combat_score: str
    kill_deaths: str
    kill_assists_survived_traded: str
    average_damage_per_round: str
    kills_per_round: str
    assists_per_round: str
    first_kills_per_round: str
    first_deaths_per_round: str
    headshot_percentage: str
    clutch_success_percentage: str


class DetailedPlayerData(BaseModel):
    status: int
    segments: list[PlayerStat]


class DetailedPlayerStats(BaseModel):
    data: DetailedPlayerData
