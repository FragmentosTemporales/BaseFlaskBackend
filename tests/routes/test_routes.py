import unittest
from tests import BaseTestCase


class TestUsuarioModel(BaseTestCase):
    """ Tests para el endpoint de usuario o general """

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Acceder al mensaje desde el JSON
        data = response.get_json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Welcome to the Flask API!")


# Ejecutar pruebas
if __name__ == '__main__':
    unittest.main()
