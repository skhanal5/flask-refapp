from flask_refapp.adapters.vlr_adapter import VLRAdapter


class ValorantService:
    def __init__(self):
        self._adapter = VLRAdapter()

    def get_health(self):
        self._adapter.get_health_status()
