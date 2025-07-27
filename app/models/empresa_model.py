from .db import db, Base


class Empresa(Base):
    __tablename__ = 'empresa'
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(250), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)

    areas = db.relationship('Area', back_populates='empresa')


class Area(Base):
    __tablename__ = 'area'
    nombre = db.Column(db.String(100), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey(
        'empresa.id'),
        nullable=False)

    empresa = db.relationship('Empresa', back_populates='areas')
    usuarios = db.relationship('Usuario', back_populates='area')

    @classmethod
    def find_by_empresa(cls, empresa_id):
        """ Find areas by company ID """
        return cls.query.filter_by(empresa_id=empresa_id).all()
