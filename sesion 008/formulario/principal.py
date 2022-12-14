from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/resultado", methods=['POST', 'GET'])
def resultado():
    if request.method == 'POST':
        data = request.form
        usuario = data['nombre'] + " " + data['apellido']

        return render_template("resultado.html", datos = data, usuario = usuario)
    else:
        return redirect(url_for('index'))

app.run()