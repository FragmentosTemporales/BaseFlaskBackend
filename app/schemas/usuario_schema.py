from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from ..models import db, Usuario, Rol

ma = Marshmallow()


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class UsuarioSchema(BaseSchema):
    proyectos = fields.Nested('ProyectoSchema', many=True)
    rol = fields.Nested('RolSchema')

    class Meta(BaseSchema.Meta):
        model = Usuario
        load_instance = True
        include_fk = True

    correo = fields.Email(
        required=True,
        validate=[
            validate.Length(
                min=5,
                max=100,
                error="El correo debe tener entre 5 y 100 caracteres"),
            validate.Email(
                error="Formato de correo inválido")
        ]
    )

    clave = fields.String(
        required=True,
        load_only=True,  # Solo para cargar datos, no para serializar
        validate=[
            validate.Length(
                min=8, max=128,
                error="La contraseña debe tener entre 8 y 128 caracteres"),
        ]
    )

    nombre = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=2,
                max=250,
                error="El nombre debe tener entre 2 y 250 caracteres"),
            validate.Regexp(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                error="El nombre solo puede contener letras y espacios"
            )
        ]
    )

    numDoc = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=7,
                max=20,
                error="El formato debe ser 17523395-4"),
        ]
    )


class RolSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Rol
        load_instance = True

    nombre = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=2,
                max=100,
                error="El nombre del rol debe tener entre 2 y 100 caracteres"),
            validate.Regexp(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                error="El nombre del rol solo puede contener letras y espacios"
            )
        ]
    )

    descripcion = fields.String(
        required=False,
        validate=validate.Length(
            max=250,
            error="La descripción no puede exceder los 250 caracteres")
    )


# Instancias de los esquemas
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

rol_schema = RolSchema()
roles_schema = RolSchema(many=True)
