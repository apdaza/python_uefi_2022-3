from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<nombre>")
def principal(nombre):
    lenguajes = {'python' : 'excelente', 
                 'java' : 'bueno pero complejo',
                 'php' : 'fácil pero mal usado'}
    return render_template('index.html', usuario = nombre, data = lenguajes)

app.run()