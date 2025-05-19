import unittest
from tests import BaseTestCase
from tests.utils.usuario import save_usuario_to_db
from app.schemas import UsuarioSchema


usuario_schema = UsuarioSchema()


class TestUsuarioModel(BaseTestCase):
    """ Test that usuario model is ok """

    def setUp(self):
        """ Setting up the test class  """
        super().setUp()
        self.data = {
            "correo": "example@example.com",
            "clave": "12345",
        }
        self.data_correo_upper = {
            "correo": "correo@EXAMPLE.COM",
            "clave": "12345",
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
        self.assertIsNotNone(user.usuarioID)
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
