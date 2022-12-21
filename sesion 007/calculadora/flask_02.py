from flask import Flask
from calculadora import Calculadora

app = Flask(__name__)

@app.route("/suma/<int:v1>/<int:v2>")
def suma(v1, v2):
    c = Calculadora(v1, v2)
    c.suma()
    return c.respuesta()

@app.route("/resta/<int:v1>/<int:v2>")
def resta(v1, v2):
    c = Calculadora(v1, v2)
    c.resta()
    return c.respuesta()

app.run(debug = True)