from httpx import Response

from vleague_backend.adapters.vlr_adapter import VLRAdapter


class ValorantService:
    def __init__(self):
        self._adapter = VLRAdapter()

    def get_health(self) -> Response:
        return self._adapter.get_health()
