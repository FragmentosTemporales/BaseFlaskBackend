from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from marshmallow import fields, validate, validates, validates_schema, ValidationError
import re
from ..models import Usuario, db

ma = Marshmallow()


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class UsuarioSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Usuario
        load_instance = True

    correo = fields.Email(
        required=True,
        validate=[
            validate.Length(min=5, max=100, error="El correo debe tener entre 5 y 100 caracteres"),
            validate.Email(error="Formato de correo inválido")
        ]
    )

    clave = fields.String(
        required=True,
        load_only=True,  # Solo para cargar datos, no para serializar
        validate=[
            validate.Length(min=8, max=128, error="La contraseña debe tener entre 8 y 128 caracteres"),
        ]
    )

    nombre = fields.String(
        required=True,
        validate=[
            validate.Length(min=2, max=250, error="El nombre debe tener entre 2 y 250 caracteres"),
            validate.Regexp(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                error="El nombre solo puede contener letras y espacios"
            )
        ]
    )

    numDoc = fields.String(
        required=True,
        validate=[
            validate.Length(min=7, max=20, error="El número de documento debe tener entre 7 y 20 caracteres"),
        ]
    )


# Esquema para actualización (campos opcionales)
class UsuarioUpdateSchema(UsuarioSchema):
    class Meta(UsuarioSchema.Meta):
        pass

    # Hacer campos opcionales para actualización
    correo = fields.Email(
        validate=[
            validate.Email()
        ]
    )

    nombre = fields.String(
        validate=[
            validate.Length(min=2, max=250),
            validate.Regexp(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')
        ]
    )

    numDoc = fields.String(
        validate=[
            validate.Length(min=7, max=20)
        ]
    )


# Instancias de los esquemas
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
usuario_update_schema = UsuarioUpdateSchema()
usuarios_update_schema = UsuarioUpdateSchema(many=True)
