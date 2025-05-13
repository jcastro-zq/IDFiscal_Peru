from flask import Blueprint, request, jsonify
import requests
from bs4 import BeautifulSoup

SunatRoutes = Blueprint('SunatRoutes', __name__)

@SunatRoutes.route('/', methods=['GET'])
def consulta_ruc():
    ruc = request.args.get("ruc")
    if not ruc:
        return jsonify({"error": "Falta el RUC"}), 400

    try:
        session = requests.Session()
        headers = {"User-Agent": "Mozilla/5.0"}

        session.get("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/frameCriterioBusqueda.jsp", headers=headers)

        url = f"https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias?accion=consPorRuc&nroRuc={ruc}&codigo=12345678"
        response = session.get(url, headers=headers)

    print("===== HTML devuelto por SUNAT =====")
        print(response.text)
        print("===== FIN DEL HTML =====")
        
        soup = BeautifulSoup(response.text, "html.parser")

        tabla = soup.find("table", class_="form-table")
        if not tabla:
            return jsonify({"estado": "No encontrado", "ruc": ruc})

        razon_social = tabla.find_all("tr")[0].find_all("td")[1].text.strip()

        return jsonify({
            "ruc": ruc,
            "razon_social": razon_social,
            "estado": "Encontrado"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
