from werkzeug.security import generate_password_hash, check_password_hash
from .db import db, Base


class Usuario(Base):
    """ SQLAlchemy model for Usuario 
    This model represents a user in the system with attributes such as correo, clave, nombre, and numDoc.
    It includes methods for setting and checking the password, finding a user by correo, and checking if a user exists.
    It also includes a method to save the user to the database.
    Attributes:
        correo (str): The user's email address.
        clave (str): The user's password.
        nombre (str): The user's name.
        numDoc (str): The user's document number.
    Methods:
        set_clave(clave): Sets the user's password after hashing it.
        set_correo_lower(correo): Sets the user's email address in lowercase.
        check_clave(clave): Checks if the provided password matches the stored hashed password.
        find_by_correo(correo): Finds a user by their email address.
        exists(correo): Checks if a user with the given email address exists in the database
    """
    __tablename__ = 'usuario'
    correo = db.Column(db.String(100), nullable=False)
    clave = db.Column(db.String(250), nullable=False)
    nombre = db.Column(db.String(250), nullable=False)
    numDoc = db.Column(db.String(20), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id', ondelete='CASCADE'), nullable=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id', ondelete='CASCADE'), nullable=False)

    proyectos = db.relationship('Proyecto', back_populates='usuario')
    area = db.relationship('Area', back_populates='usuarios')
    rol = db.relationship('Rol', back_populates='usuarios')

    def set_clave(self, clave):
        """ Setting clave for usuario """
        self.clave = generate_password_hash(clave)

    def set_correo_lower(self, correo):
        """Setting the lowercase correo"""
        self.correo = correo.lower()

    def check_clave(self, clave):
        """ Checking clave for usuario """
        return check_password_hash(self.clave, clave)

    @classmethod
    def find_by_correo(cls, correo):
        """ Find user by correo address """
        correo_lower = correo.lower()
        return cls.query.filter_by(correo=correo_lower).first()

    @classmethod
    def find_all_by_empresa(cls, empresa_id):
        """ Find all users by empresa ID """
        return cls.query.filter_by(empresa_id=empresa_id).all()

    @staticmethod
    def exists(correo):
        """ Check if user exists """
        correo_lower = correo.lower()
        usuario = Usuario.find_by_correo(correo_lower)

        if usuario:
            return True
        return False


class Rol(Base):
    """ SQLAlchemy model for Rol
    This model represents a role in the system with attributes such as nombre and descripcion.
    It includes methods to save the role to the database and retrieve all roles.
    Attributes:
        nombre (str): The name of the role.
        descripcion (str): A description of the role.
    """
    __tablename__ = 'rol'
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)

    usuarios = db.relationship('Usuario', back_populates='rol')

    @classmethod
    def find_all(cls):
        """ Find all roles """
        return cls.query.all()  
