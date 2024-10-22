import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import unittest

from src.calculadora import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular


class TestCalculadora(unittest.TestCase):

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])

    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([5]), 5)

    def test_media_dos_elementos(self):
        self.assertEqual(calcular_media([5, 10]), 7.5)

    def test_media_n_elementos_positivos(self):
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)

    def test_media_n_elementos_ceros(self):
        self.assertEqual(calcular_media([0, 0, 0]), 0)

    def test_media_n_elementos_positivos_negativos(self):
        self.assertEqual(calcular_media([1, -1, 2, -2]), 0)

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_media([1, "a", 3])

    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0)

    def test_desviacion_estandar_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([5, 10]), 2.5)

    def test_desviacion_estandar_n_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1, 2, 3, 4, 5]), 1.41421356237)


if __name__ == '__main__':
    unittest.main()
