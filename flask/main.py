from domains.advices.routes import advices_bp
from domains.hello.routes import hello_bp
from flask import Flask, jsonify, request

app = Flask(__name__)

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
