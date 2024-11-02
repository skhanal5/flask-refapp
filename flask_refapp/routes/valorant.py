from flask import Blueprint

from flask_refapp.services.valorant_service import ValorantService

valorant_bp = Blueprint("valorant", __name__, url_prefix="/val")


@valorant_bp.route("/health")
def get_health():
    # TODO: Make a singleton instance
    service = ValorantService()
    return service.get_health()