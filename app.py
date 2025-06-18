from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/processar', methods=['POST'])
def processar():
    dados = request.json
    # Lógica aqui...
    return jsonify({"status": "sucesso", "dados_recebidos": dados})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
