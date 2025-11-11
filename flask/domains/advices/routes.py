from flask import Blueprint, jsonify
from shared.domains.advices.external_service import ExternalAdviceService
from shared.domains.advices.schemas import AdviceRead
from shared.domains.advices.service import AdviceService

advices_bp = Blueprint("advices", __name__, url_prefix="/advices")

# Endpoint para obter um conselho aleatório
@advices_bp.route("/", methods=["GET"])
def get_advice():
    advice = ExternalAdviceService.get_advice()
    response = AdviceRead(
        id=advice.slip.id,
        advice=advice.slip.advice
    )
    return jsonify(response.dict())

# Endpoint para obter a contagem total de conselhos
@advices_bp.route("/count", methods=["GET"])
def get_advice_count():
    service = AdviceService()
    response = service.get_advice_count()
    return jsonify(response.dict())
