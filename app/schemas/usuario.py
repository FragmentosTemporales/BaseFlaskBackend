from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from ..models import Usuario, db

ma = Marshmallow()


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class UsuarioSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Usuario
        clave = auto_field(load_only=True)


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
