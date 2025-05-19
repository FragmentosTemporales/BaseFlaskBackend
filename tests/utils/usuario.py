from app.models import Usuario


def save_usuario_to_db(data):
    """ Save usuario to db """
    clave = data.get("clave", None)
    correo = data.get("correo", None)
    usuario = Usuario(**data)
    usuario.set_clave(clave)
    usuario.set_correo_lower(correo)

    exist = usuario.exists(correo)

    if exist:
        return {"error": "Email already exists"}, 400
    else:
        usuario.save_to_db()

    return usuario
