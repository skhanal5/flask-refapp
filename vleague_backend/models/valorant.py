from pydantic import BaseModel


class TeamRequest(BaseModel):
    team: str


class PlayerRequest(BaseModel):
    player: str
