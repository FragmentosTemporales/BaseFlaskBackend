from .db import db, Base


class Proyecto(Base):
    """ SQLAlchemy model for Proyecto
    This model represents a project in the system with attributes such as nombre, descripcion, and fecha_inicio.
    It includes methods to save the project to the database and retrieve all projects.
    Attributes:
        nombre (str): The name of the project.
        descripcion (str): A description of the project.
    """
    __tablename__ = 'proyecto'
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='proyectos')
    tareas = db.relationship('Tarea', back_populates='proyecto')

    @classmethod
    def find_by_usuario(cls, usuario_id):
        """ Find projects by user ID """
        return cls.query.filter_by(usuario_id=usuario_id).all()


class Tarea(Base):
    """ SQLAlchemy model for Tarea
    This model represents a task in the system with attributes such as titulo, descripcion, fecha_creacion, and estado.
    It includes methods to save the task to the database and retrieve all tasks.
    Attributes:
        titulo (str): The title of the task.
        descripcion (str): A description of the task.
        fecha_creacion (datetime): The creation date of the task.
        estado (str): The status of the task (e.g., 'pendiente', 'completada').
    """
    __tablename__ = 'tarea'
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id', ondelete='CASCADE'), nullable=False)

    proyecto = db.relationship('Proyecto', back_populates='tareas')
    estado_tarea = db.relationship('EstadoTarea', back_populates='tarea')


class EstadoTarea(Base):
    """ SQLAlchemy model for EstadoTarea
    This model represents the status of a task in the system with attributes such as descripcion.
    It includes methods to save the status to the database and retrieve all statuses.
    Attributes:
        descripcion (str): A description of the task status.
        tarea_id (int): The ID of the task to which this status belongs.
    """
    __tablename__ = 'estado_tarea'
    descripcion = db.Column(db.String(50), nullable=False)
    tarea_id = db.Column(db.Integer, db.ForeignKey('tarea.id', ondelete='CASCADE'), nullable=False)

    tarea = db.relationship('Tarea', back_populates='estado_tarea')

    @classmethod
    def find_last_by_tarea(cls, tarea_id):
        """ Find the last status of a task by task ID """
        return cls.query.filter_by(tarea_id=tarea_id).order_by(cls.id.desc()).first()

    @classmethod
    def find_by_tarea(cls, tarea_id):
        """ Find all statuses of a task by task ID """
        return cls.query.filter_by(tarea_id=tarea_id).order_by(cls.fecha_registro.desc()).all()
