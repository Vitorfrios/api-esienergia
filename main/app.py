from flask import Flask, request, send_file
from pdfs import PC_pdf
import io

app = Flask(__name__)

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    dados = request.json
    pdf_bytes = PC_pdf.gerar_pdf(dados)
    return send_file(io.BytesIO(pdf_bytes), download_name="proposta.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)