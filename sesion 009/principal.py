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

class Nota(db.Model):
    id = db.Column('nota_id', db.Integer, primary_key = True)
    estudiante = db.Column(db.Integer)
    valor = db.Column(db.Integer)

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

@app.route("/editar_estudiante", methods=['POST', 'GET'])
def editar_estudiante():
    if request.method == 'GET':
        id = request.args.get('id')
        e = Estudiante.query.filter_by(id = id).first()
        return render_template('editar_estudiante.html', datos = e)
    else:
        formulario = request.form
        id = formulario['id']
        e = Estudiante.query.filter_by(id = id).first()
        e.nombre = formulario['nombre']
        e.apellido = formulario['apellido']
        e.correo = formulario['correo']
        e.codigo = formulario['codigo']
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/eliminar_estudiante", methods=['POST', 'GET'])
def eliminar_estudiante():
    if request.method == 'GET':
        id = request.args.get('id')
        e = Estudiante.query.filter_by(id = id).first()
        return render_template('eliminar_estudiante.html', datos = e)
    else:
        id = request.form['id']
        e = Estudiante.query.filter_by(id = id).first()
        db.session.delete(e)
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/ver_notas", methods=['GET'])
def ver_notas():
    if request.method == 'GET':
        id = request.args.get('id')
        e = Estudiante.query.filter_by(id = id).first()
        n = Nota.query.filter_by(estudiante = id).all()

        return render_template('ver_notas.html', estudiante = e, notas = n)

# cargamos la aplicacion
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug = True)