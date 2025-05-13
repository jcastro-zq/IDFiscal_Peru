from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'API Peru RUC funcionando'

@app.route('/consulta', methods=['GET'])
def consulta():
    ruc = request.args.get('ruc')
    if not ruc:
        return jsonify({"error": "Debe proporcionar un RUC"}), 400

    if ruc == "20100070970":
        resultado = {
            "ruc": ruc,
            "razon_social": "SUPERMERCADOS PERUANOS SOCIEDAD ANONIMA",
            "estado": "ACTIVO",
            "condicion": "HABIDO"
        }
    else:
        resultado = {
            "ruc": ruc,
            "estado": "No encontrado"
        }

    response = jsonify(resultado)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
