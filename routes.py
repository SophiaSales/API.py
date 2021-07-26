from flask import Flask

app = Flask("Hello Word")

@app.route("/", methods=["GET"])
def olaMundo():
    return{"ola": "mundo"}

app.run()