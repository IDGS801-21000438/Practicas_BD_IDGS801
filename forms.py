from wtforms import Form,StringField, EmailField, IntegerField, validators



class EmpleadosForm( Form ):

    id = IntegerField('id',[validators.number_range(min=1, max=20, message='valor requerido')])
    nombre = StringField('nombre',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa nombre valido")])
    direccion = StringField('nombre',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa nombre valido")])
    telefono = StringField('nombre',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa nombre valido")])
    correo = EmailField('email',[validators.Email(message="Ingresa un correo valido")])
    sueldo = IntegerField('nombre',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa nombre valido")])
  