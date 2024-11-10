# from httpx import Response
#
# from vleague_backend.models.vlr_orl import AllTeamsResponse
# from vleague_backend.port.valorant_port import ValorantPort
#
#
# class ValorantService:
#     def __init__(self, port: ValorantPort):
#         self.port = port
#
#     def get_health(self) -> Response:
#         return self.port.get_health()
#
#     def get_teams(self) -> AllTeamsResponse:
#         return self.port.get_all_teams
#
#     def get_team(self, team:str):
#         return self.port.get
