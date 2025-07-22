from flask.cli import FlaskGroup
from app import create_app
import click
import logging
from rich import print
from app.schemas import *
from app.models.usuario_model import Usuario
from app.models.proyecto_model import Proyecto, Tarea
from app.sql import MyEngine


cli = FlaskGroup(create_app=create_app)


@cli.command("create-user")
@click.option("--correo", required=True)
@click.option("--clave", required=True)
@click.option("--nombre", required=True)
@click.option("--numdoc", required=True)
def create_user(correo, clave, nombre, numdoc):  # <-- aquí en minúsculas
    """ Create user in the platform by command line interface """
    # python manage.py create-user --correo=cristian.example@correo.com --clave=Clave123. --nombre=Cristian --numdoc=17523395-4

    try:
        user_data = {
            "correo": correo.lower(),
            "clave": clave,
            "nombre": nombre,
            "numDoc": numdoc
        }
        user_obj = usuario_schema.load(user_data)
        user_obj.set_clave(clave)
        user_obj.set_correo_lower(correo)

        exist = user_obj.exists(correo)

        if exist:
            print("El correo ya existe.")
        else:
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


@cli.command("user")
def ejecutador_user() -> dict:
    try:
        user_data = {
            "correo": "example@mail.com",
            "clave": "123456qwerty",
            "nombre": "Example User",
            "numDoc": "12345678-9",
            "area_id": 1,
            "rol_id": 1,
        }
        user_obj = usuario_schema.load(user_data)
        user_obj.set_clave(user_obj.clave)
        user_obj.set_correo_lower(user_obj.correo)

        exist = user_obj.exists(user_obj.correo)

        if exist:
            print("El correo ya existe.")
        else:
            user_obj.save_to_db()
            print("Usuario creado correctamente.")
    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)

@cli.command("emp")
def ejecutador_emp() -> dict:
    try:
        empresa_data = {
            "nombre": "Example User",
            "direccion": "example@mail.com",
            "telefono": "123456qwerty"
        }
        empresa_obj = empresa_schema.load(empresa_data)
        empresa_obj.save_to_db()
        print("[bold red] # Empresa creada correctamente  # [/bold red]")

    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)

@cli.command("rol")
def ejecutador_rol() -> dict:
    try:
        empresa_data = {
            "nombre": "Administrador",
            "descripcion": "Rol de administrador del sistema"
        }
        empresa_obj = rol_schema.load(empresa_data)
        empresa_obj.save_to_db()
        print("[bold red] # Rol creado correctamente  # [/bold red]")

    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)

@cli.command("area")
def ejecutador_area() -> dict:
    try:
        empresa_data = {
            "nombre": "Example Area",
            "empresa_id": 1
        }
        empresa_obj = area_schema.load(empresa_data)
        empresa_obj.save_to_db()
        print("[bold red] # Area creada correctamente  # [/bold red]")

    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)


@cli.command("proyecto")
def ejecutador_proyecto() -> dict:
    try:
        proyecto_data = {
            "nombre": "Proyecto de Ejemplo",
            "descripcion": "Descripción del proyecto de ejemplo",
            "usuario_id": 1
        }
        proyecto_obj = proyecto_schema.load(proyecto_data)
        proyecto_obj.save_to_db()
        print("[bold red] # Proyecto creado correctamente  # [/bold red]")

    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)

@cli.command("tarea")
def ejecutador_tarea() -> dict:
    try:
        tarea_data = {
            "titulo": "Tarea de Ejemplo 2",
            "descripcion": "Descripción de la tarea de ejemplo 2",
            "proyecto_id": 1
        }
        tarea_obj = tarea_schema.load(tarea_data)
        tarea_obj.save_to_db()
        print("[bold red] # Tarea creada correctamente  # [/bold red]")

    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)

@cli.command("estado_tarea")
def ejecutador_estado_tarea() -> dict:
    try:
        estado_tarea_data = {
            "descripcion": "En progreso",
            "tarea_id": 2
        }
        estado_tarea_obj = estado_tarea_schema.load(estado_tarea_data)
        estado_tarea_obj.save_to_db()
        print("[bold red] # Estado de tarea creado correctamente  # [/bold red]")

    except Exception as e:
        print(f"Error de validación: {e}")
        return str(e)

@cli.command("sql")
def sql_executor():
    """ Ejecuta una consulta SQL """
    try:
        engine = MyEngine()
        query = "SELECT * FROM usuario;"
        result = engine.query(query)
        print(f"[bold blue]{result}[/bold blue]")
    except Exception as e:
        print(f"Error al ejecutar la consulta SQL: {e}")

@cli.command("get")
def db_executor():
    """ Ejecuta una consulta SQL para crear tablas """
    try:
        empresa_data = Empresa.find_by_id(1)
        empresa = empresa_schema.dump(empresa_data)
        print(f"[bold green] # Empresa: {empresa}  # [/bold green]")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

if __name__ == "__main__":
    cli()
