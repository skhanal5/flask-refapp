from httpx import Response

from flask_refapp.adapters.vlr_adapter import VLRAdapter


class ValorantService:
    def __init__(self, adapter: VLRAdapter = None):
        self._adapter = adapter or VLRAdapter()

    def get_health(self) -> Response:
        return self._adapter.get_health_status()
