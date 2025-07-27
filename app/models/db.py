from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime as dt

# Inicialización de db y migrate
db = SQLAlchemy()
migrate = Migrate()


class Base(db.Model):
    """Model that contains base database models."""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_registro = db.Column(
        db.DateTime, nullable=False, default=lambda: dt.datetime.now(
            dt.UTC))

    def save_to_db(self):
        """Save instance to the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, **kwargs):
        """Update instance in the database."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_from_db(self):
        """Delete instance from the database."""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        """ Get all from db """
        return cls.query.order_by(cls.fecha_registro.desc()).all()

    @classmethod
    def find_by_id(cls, id):
        """ Find data by id """
        return cls.query.filter_by(id=id).first()
