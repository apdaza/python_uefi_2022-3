from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# creacion del app
app = Flask(__name__)

# configuracion de parametros para sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.sqlite3'
app.config['SECRET_KEY'] = '12345qwerty'
app.config['SQLALCHEMY_TRAK_MODIFICATIONS'] = False

# creacion del objeto de base de datos
db = SQLAlchemy(app)

# definir clases para modelo de datos
class Estudiante(db.Model):
    id = db.Column('estudiante_id', db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    codigo = db.Column(db.String(15))
    correo = db.Column(db.String(50))

    def __init__(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.codigo = datos['codigo']
        self.correo = datos['correo']

# definimos las rutas de nuestra aplicacion
@app.route("/")
def index():
    return render_template("index.html", datos = Estudiante.query.all())

@app.route("/agregar_estudiante", methods=['POST', 'GET'])
def agregar_estudiante():
    if request.method == 'POST':
        formulario = request.form
        nombre = formulario['nombre']
        apellido = formulario['apellido']
        codigo = formulario['codigo']
        correo = formulario['correo']
        datos = {
            'nombre': nombre,
            'apellido': apellido,
            'codigo': codigo,
            'correo': correo
        }
        e = Estudiante(datos)
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('agregar_estudiante.html')

# cargamos la aplicacion
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug = True)