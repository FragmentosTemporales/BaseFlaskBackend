from .db import db, Base


class Empresa(Base):
    """ SQLAlchemy model for Empresa
    This model represents a company in the system with attributes such as nombre, direccion, and telefono.
    It includes methods to save the company to the database and retrieve all companies.
    Attributes:
        nombre (str): The name of the company.
        direccion (str): The address of the company.
        telefono (str): The phone number of the company.
    """
    __tablename__ = 'empresa'
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(250), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)

    areas = db.relationship('Area', back_populates='empresa')


class Area(Base):
    """ SQLAlchemy model for Area
    This model represents an area within a company with attributes such as nombre and empresa_id.
    It includes methods to save the area to the database and retrieve all areas.
    Attributes:
        nombre (str): The name of the area.
        empresa_id (int): The ID of the company to which this area belongs.
    """
    __tablename__ = 'area'
    nombre = db.Column(db.String(100), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)

    empresa = db.relationship('Empresa', back_populates='areas')
    usuarios = db.relationship('Usuario', back_populates='area')

    @classmethod
    def find_by_empresa(cls, empresa_id):
        """ Find areas by company ID """
        return cls.query.filter_by(empresa_id=empresa_id).all()
