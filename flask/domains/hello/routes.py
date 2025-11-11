from flask import Blueprint
from shared.domains.hello.services import HelloService

hello_bp = Blueprint("/", __name__)

@hello_bp.route("/", methods=["GET"])
def home():
    return HelloService.get_greeting()
