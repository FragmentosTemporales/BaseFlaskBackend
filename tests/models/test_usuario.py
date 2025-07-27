import unittest
from tests import BaseTestCase
from tests.utils.usuario import save_usuario_to_db
from app.schemas import UsuarioSchema
from app.models import Rol


usuario_schema = UsuarioSchema()


class TestUsuarioModel(BaseTestCase):
    """ Test that usuario model is ok """

    def setUp(self):
        """ Setting up the test class  """
        super().setUp()

        # Create a test role first
        test_rol = Rol(nombre="Test Role", descripcion="Role for testing")
        test_rol.save_to_db()

        self.data = {
            "correo": "example@example.com",
            "clave": "password123.",
            "nombre": "Test Usuario",
            "numDoc": "12345678",
            "rol_id": test_rol.id
        }
        self.data_correo_upper = {
            "correo": "correo@EXAMPLE.COM",
            "clave": "password123.",
            "nombre": "Test Usuario Upper",
            "numDoc": "87654321",
            "rol_id": test_rol.id
        }
        self.params = {
            "correo": "test@test.com",
        }

    def test_string_representation(self):
        """ Test string representation of usuario model """
        clave = self.data.get("clave", None)
        usuario = usuario_schema.load(self.data)
        self.assertEqual(clave, usuario.clave)

    def test_create_success(self):
        """ Test create user is success """
        user = save_usuario_to_db(self.data)
        self.assertIsNotNone(user.id)
        for key in self.data.keys():
            if key != "clave":
                self.assertEqual(
                    getattr(user, key), self.data.get(key, None))
        self.assertTrue(user.check_clave(self.data.get("clave", None)))

    def test_create_fails_because_email_already_taken(self):
        """ Test create user fails because email already taken """
        save_usuario_to_db(self.data)
        res = save_usuario_to_db(self.data)
        error = "Email already exists"
        mssge = res[0]['error']
        self.assertEqual(error, mssge)

    def test_email_normalized(self):
        """ Test user email is normalized after save into db """
        user = save_usuario_to_db(self.data_correo_upper)
        self.assertEqual(user.correo, self.data_correo_upper["correo"].lower())


if __name__ == "__main__":
    unittest.main()
