from domains.advices.routes import advices_bp
from domains.hello.routes import hello_bp
from flasgger import Swagger
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Carrega template externo
with open("docs/openapi_template.json") as f:
    swagger_template = json.load(f)

swagger = Swagger(app, template=swagger_template)

# Rota com parâmetro
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    query = request.args.get("q")
    return jsonify({"item_id": item_id, "query": query})

# Registra o blueprint
app.register_blueprint(hello_bp)
app.register_blueprint(advices_bp)

if __name__ == "__main__":
    app.run(debug=True)
