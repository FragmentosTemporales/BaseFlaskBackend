from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from ..models import db, Empresa, Area 

ma = Marshmallow()


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class EmpresaSchema(BaseSchema):
    areas = fields.Nested('AreaSchema', many=True)

    class Meta(BaseSchema.Meta):
        model = Empresa
        include_fk = True


class AreaSchema(BaseSchema):
    usuarios = fields.Nested('UsuarioSchema', many=True)

    class Meta(BaseSchema.Meta):
        model = Area
        include_fk = True


empresa_schema = EmpresaSchema()
empresas_schema = EmpresaSchema(many=True)

area_schema = AreaSchema()
areas_schema = AreaSchema(many=True)