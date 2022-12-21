from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola mundo en flask"

@app.route("/hola/<nombre>")
def hola_saludo(nombre):
    return "Hola %s" % nombre

@app.route("/repetidor/<int:cantidad>/<palabra>")
def repetidor(cantidad, palabra):
    return palabra * cantidad

app.run()