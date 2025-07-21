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

    @staticmethod
    def exists(correo):
        """ Check if user exists """
        correo_lower = correo.lower()
        usuario = Usuario.find_by_correo(correo_lower)

        if usuario:
            return True
        return False
