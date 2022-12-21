from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def hola_admin():
    return "hola admin"

@app.route("/invitado/<nombre>")
def hola_invitado(nombre):
    return "hola %s ingresaste como invitado" %nombre

@app.route("/<usuario>")
def inicio(usuario):
    if usuario == "admin":
        return redirect(url_for("hola_admin"))
    else:
        return redirect(url_for("hola_invitado", nombre = usuario))

app.run()
