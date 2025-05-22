from werkzeug.security import generate_password_hash, check_password_hash
from .db import db, Base


class Usuario(Base):
    __tablename__ = 'usuario'
    usuarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String(100), nullable=False)
    clave = db.Column(db.String(250), nullable=False)

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
    def find_by_id(cls, usuarioID):
        """ Find user by correo address """
        id = usuarioID
        return cls.query.filter_by(usuarioID=id).first()

    @staticmethod
    def exists(correo):
        """ Check if user exists """
        correo_lower = correo.lower()
        usuario = Usuario.find_by_correo(correo_lower)

        if usuario:
            return True
        return False
