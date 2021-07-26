from flask import Flask

app = Flask("Hello Word")

@app.route("/", methods=["GET"])
def olaMundo():
    return{"ola": "mundo"}

@app.route("/cadastro", methods=["POST"])
def cadastro():
    return{"id": 0}    

app.run()