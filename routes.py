from flask import Flask, request
from flask.wrappers import Response

# importaçao da funçao
from main import sensorTemp

app = Flask("Hello Word")

# rota get 
@app.route("/", methods=["GET"])
def olaMundo():
    return sensorTemp

# rota post 
@app.route("/cadastro", methods=["POST"])
def cadastro():

# mandar prametros para o body 
    body = request.get_json()

# tratativa de erro
    if("temperatura" not in body):
        return retornoValores(400, "Erro na gravaçao da temperatura")

    if("humidade" not in body):
        return retornoValores(400, "Erro na gravaçao da humidade")
# variavel contendo a funçao do sensor para retornar valores pelo body
    sensor = sensorTemp(body["temperatura"], body["humidade"])

# resposta da requisiçao 
    return retornoValores(200, "dados recebidos", "sensortmp" ,sensor)

# funçao retornando valores do sensor como mensagem em json
def retornoValores(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

# quando o conteudo nao for falso, adiciona o conteudo 
    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response
app.run()