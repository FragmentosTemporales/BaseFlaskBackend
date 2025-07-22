from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from ..models import Proyecto, db, Tarea, EstadoTarea

ma = Marshmallow()


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        sqla_session = db.session


class ProyectoSchema(BaseSchema):
    tareas = fields.Nested(
        'TareaSchema',
        many=True)

    class Meta(BaseSchema.Meta):
        model = Proyecto
        include_fk = True


class TareaSchema(BaseSchema):
    estado_tarea = fields.Nested(
        'EstadoTareaSchema',
        many=True)

    class Meta(BaseSchema.Meta):
        model = Tarea
        include_fk = True


class EstadoTareaSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = EstadoTarea
        include_fk = True


proyecto_schema = ProyectoSchema()
proyectos_schema = ProyectoSchema(many=True)
tarea_schema = TareaSchema()
tareas_schema = TareaSchema(many=True)
estado_tarea_schema = EstadoTareaSchema()
estados_tarea_schema = EstadoTareaSchema(many=True)
