from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import datetime

db = SQLAlchemy()


class Empleados(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    sueldo = db.Column(db.Integer)




    