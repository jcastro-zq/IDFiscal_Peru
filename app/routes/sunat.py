from flask import Blueprint, request, jsonify
import requests
from bs4 import BeautifulSoup

SunatRoutes = Blueprint('SunatRoutes', __name__)

@SunatRoutes.route('/', methods=['GET'])
def consulta_sunat():
    ruc = request.args.get("ruc")
    if not ruc:
        return jsonify({"error": "Falta el RUC"}), 400

    try:
        url = f"https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias?accion=consPorRuc&nroRuc={ruc}&codigo=123"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        td = soup.find("td", string="Nombre o Razón Social")
        if not td:
            return jsonify({"ruc": ruc, "estado": "No encontrado"}), 404

        razon_social = td.find_next("td").text.strip()
        return jsonify({
            "ruc": ruc,
            "razon_social": razon_social,
            "estado": "Encontrado"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
