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


if __name__ == "__main__":
    unittest.main()
