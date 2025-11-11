from flask import Blueprint, jsonify
from shared.domains.advices.external_service import ExternalAdviceService
from shared.domains.advices.schemas import AdviceRead

advices_bp = Blueprint("advices", __name__, url_prefix="/advices")

@advices_bp.route("/", methods=["GET"])
def get_advice():
    advice = ExternalAdviceService.get_advice()
    response = AdviceRead(
        id=advice.slip.id,
        advice=advice.slip.advice
    )
    return jsonify(response.dict())
