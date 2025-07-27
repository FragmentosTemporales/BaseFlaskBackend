from .db import db, Base


class Proyecto(Base):
    __tablename__ = 'proyecto'
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'usuario.id',
        ondelete='CASCADE'),
        nullable=False)

    usuario = db.relationship('Usuario', back_populates='proyectos')
    tareas = db.relationship('Tarea', back_populates='proyecto')

    @classmethod
    def find_by_usuario(cls, usuario_id):
        """ Find projects by user ID """
        return cls.query.filter_by(usuario_id=usuario_id).all()


class Tarea(Base):
    __tablename__ = 'tarea'
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)
    proyecto_id = db.Column(db.Integer, db.ForeignKey(
        'proyecto.id',
        ondelete='CASCADE'),
        nullable=False)

    proyecto = db.relationship('Proyecto', back_populates='tareas')
    estado_tarea = db.relationship('EstadoTarea', back_populates='tarea')


class EstadoTarea(Base):
    __tablename__ = 'estado_tarea'
    descripcion = db.Column(db.String(50), nullable=False)
    tarea_id = db.Column(db.Integer, db.ForeignKey(
        'tarea.id',
        ondelete='CASCADE'),
        nullable=False)

    tarea = db.relationship('Tarea', back_populates='estado_tarea')

    @classmethod
    def find_last_by_tarea(cls, tarea_id):
        """ Find the last status of a task by task ID """
        return cls.query.filter_by(
            tarea_id=tarea_id).order_by(
                cls.id.desc()).first()

    @classmethod
    def find_by_tarea(cls, tarea_id):
        """ Find all statuses of a task by task ID """
        return cls.query.filter_by(
            tarea_id=tarea_id).order_by(
                cls.fecha_registro.desc()).all()
