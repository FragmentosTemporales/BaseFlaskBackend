from werkzeug.security import (
    generate_password_hash,
    check_password_hash)
from .db import db, Base


class Usuario(Base):
    __tablename__ = 'usuario'
    correo = db.Column(db.String(100), nullable=False)
    clave = db.Column(db.String(250), nullable=False)
    nombre = db.Column(db.String(250), nullable=False)
    numDoc = db.Column(db.String(20), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey(
        'area.id',
        ondelete='CASCADE'),
        nullable=True)
    rol_id = db.Column(db.Integer, db.ForeignKey(
        'rol.id',
        ondelete='CASCADE'),
        nullable=False)

    proyectos = db.relationship(
        'Proyecto',
        back_populates='usuario')
    area = db.relationship(
        'Area',
        back_populates='usuarios')
    rol = db.relationship(
        'Rol',
        back_populates='usuarios')

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
    __tablename__ = 'rol'
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)

    usuarios = db.relationship('Usuario', back_populates='rol')

    @classmethod
    def find_all(cls):
        """ Find all roles """
        return cls.query.all()
