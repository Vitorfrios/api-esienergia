from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/processar', methods=['POST'])
def processar():
    dados = request.json  # Espera receber JSON no body
    
    # Aqui você pode fazer os cálculos, validações, gerar PDFs, etc.
    # Por enquanto, só devolvendo os dados recebidos:
    
    return jsonify({
        "status": "sucesso",
        "dados_recebidos": dados,
        "mensagem": "Processamento OK!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
