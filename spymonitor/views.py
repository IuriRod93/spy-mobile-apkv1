from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/monitoramento/', methods=['POST'])
def receber_dados():
    dados = request.json
    # Aqui você pode salvar os dados no banco ou processar conforme necessário
    print("Dados recebidos:", dados)
    return jsonify({"status": "sucesso"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
