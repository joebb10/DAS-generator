from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/generate-das", methods=["POST"])
def generate_das():
    # Get the required information from the request body
     nome = request.json["nome"]
     cnpj = request.json["cnpj"]
     whatsapp = request.json["whatsapp"]

    # Get the MEI's information from the Receita Federal API
    response = requests.get("https://api.receita.fazenda.gov.br/v1/mei/cnpj/{}/info".format(cnpj))
    if response.status_code == 200:
        mei_info = response.json()
    else:
        raise Exception("Não foi possível obter as informações do MEI.")

    # Generate the DAS
    das = generate_das(mei_info)

    # Send the DAS to the WhatsApp number
    send_das_to_whatsapp(das, whatsapp)

    return "O DAS foi gerado e enviado para o WhatsApp."

def generate_das(mei_info):
    # Get the DAS information from the Receita Federal API
    response = requests.get("https://api.receita.fazenda.gov.br/v1/mei/cnpj/{}/das".format(mei_info["cnpj"]))
    if response.status_code == 200:
        das_info = response.json()
    else:
        raise Exception("Não foi possível obter as informações do DAS.")

    # Create the DAS document
    das = {
        "nome": mei_info["nome"],
        "cnpj": mei_info["cnpj"],
        "valor": das_info["valor"],
        "vencimento": das_info["vencimento"],
    }

    return das

def send_das_to_whatsapp(das, whatsapp):
    # Send the DAS document to the WhatsApp number
    requests.post("https://api.whatsapp.com/v1/send/message", data={
        "chat_id": whatsapp,
        "text": "Olá, [nome]. Aqui está o seu DAS: \n\n[das]"
    })

if __name__ == "__main__":
    app.run(debug=True)
