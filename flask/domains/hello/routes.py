from flask import Blueprint
from shared.domains.hello.services import HelloService

hello_bp = Blueprint("/", __name__)

# Endpoint para a hello world
@hello_bp.route("/", methods=["GET"])
def home():
    return HelloService.get_greeting()
