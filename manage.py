from flask.cli import FlaskGroup
from app import create_app
import click
import logging
from app.models import Usuario
from app.schemas import usuario_schema


cli = FlaskGroup(create_app=create_app)


@cli.command("create-user")
@click.option("--correo", required=True)
@click.option("--clave", required=True)
def create_user(correo, clave):
    """ Create user in the platform by command line interface """
    # python manage.py create-user --correo=correo --clave=clave

    if Usuario.exists(correo):
        print("El usuario ya existe en la base de datos.")
        return
    try:
        user_data = {
            "correo": correo.lower(),
            "clave": clave
        }
        user_obj = usuario_schema.load(user_data)
        user_obj.set_clave(clave)
        user_obj.set_correo_lower(correo)
        user_obj.save_to_db()
        print("Usuario creado correctamente.")
    except Exception as e:
        error_message = str(e)
        print(f"Printeando error: {error_message}")
        logging.error(f"Error en create_user: {error_message}")


@cli.command("test")
@click.option("--test_name")
def test(test_name=None):
    """ Runs the unit tests."""
    import unittest
    if test_name is None:
        tests = unittest.TestLoader().discover('tests', pattern="test_*.py")
    else:
        tests = unittest.TestLoader().loadTestsFromName('tests.' + test_name)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command("e")
def ejecutador():
    try:
        print("### EJECUTANDO QUERY ###")

    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    cli()
