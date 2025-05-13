from flask import Blueprint, request, jsonify

SunatRoutes = Blueprint('SunatRoutes', __name__)

@SunatRoutes.route('/', methods=['GET'])
def test_sunat():
    ruc = request.args.get("ruc")
    if not ruc:
        return jsonify({"error": "Falta el parámetro RUC"}), 400

    return jsonify({
        "status": "ok",
        "mensaje": "Este endpoint está funcionando correctamente.",
        "ruc_recibido": ruc
    })
