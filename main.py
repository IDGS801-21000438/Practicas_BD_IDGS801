from flask import Flask, render_template,request,redirect
from flask import flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms 

from models import db, Empleados

app = Flask (__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route("/empledo", methods = ["GET","POST"])
def empleado():
    empleado_clase = forms.EmpleadosForm(request.form)
    nombre = ''
    direccion = ''
    telefono = ''
    correo = ''
    sueldo = 0
    if request.method == 'POST' and empleado_clase.validate():
        nombre = empleado_clase.nombre.data
        direccion = empleado_clase.direccion.data
        telefono = empleado_clase.telefono.data
        correo = empleado_clase.correo.data
        sueldo = empleado_clase.sueldo.data



    return render_template("empleados.html",form= empleado_clase, nombre=nombre,direccion= direccion, telefono= telefono,correo= correo, sueldo=sueldo)


if __name__ =="__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()