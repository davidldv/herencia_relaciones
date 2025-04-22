import unittest
from modelo.antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):

    def test_creacion_valida(self):
        a = Antibiotico("Antibovino", 500, "Bovinos", 75000)
        self.assertEqual(a.nombre, "Antibovino")
        self.assertEqual(a.dosis, 500)
        self.assertEqual(a.tipo_animal, "Bovinos")
        self.assertEqual(a.precio, 75000)

    def test_dosis_invalida(self):
        with self.assertRaises(ValueError):
            Antibiotico("ErrorDosis", 300, "Bovinos", 50000)

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            Antibiotico("ErrorAnimal", 500, "Felinos", 50000)

if __name__ == "__main__":
    unittest.main()
