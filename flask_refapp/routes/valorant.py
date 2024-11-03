from flask import Blueprint

from flask_refapp.services.valorant_service import ValorantService

valorant_bp = Blueprint("valorant", __name__, url_prefix="/valorant")


@valorant_bp.route("/health")
def get_health() -> dict:
    # TODO: Make a singleton instance
    service = ValorantService()
    return service.get_health().json()
