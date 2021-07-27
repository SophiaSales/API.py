from flask import Flask, request

from main import sensorTemp

app = Flask("Hello Word")

@app.route("/", methods=["GET"])
def olaMundo():
    return{"ola": "mundo"}

@app.route("/cadastro", methods=["POST"])
def cadastro():

    body = request.get_json()

    if("temperatura" not in body):
        return{"status": 400, "mensagem":"Erro na gravaçao da temperatura"}

    sensor = sensorTemp(body["temperatura"], body["humidade"])

    return sensor

app.run()