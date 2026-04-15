import unittest

from src.poo_basico.persona import Persona
from src.poo_basico.saludo import Saludo


class TestSaludo(unittest.TestCase):
    def test_mensaje_por_defecto(self) -> None:
        self.assertEqual(Saludo().mensaje, "Hola mundo")


class TestPersona(unittest.TestCase):
    def test_presentarse(self) -> None:
        p = Persona(" Ana ")
        self.assertEqual(p.nombre, "Ana")
        self.assertEqual(p.presentarse(), "Me llamo Ana.")


if __name__ == "__main__":
    unittest.main()

