import pytest
import unittest


class test_003(unittest.TestCase):

    def setUp(self):
        pass

    def test_comparacion(self):
        self.Variable_A = 51
        self.Variable_B = 50

        assert self.Variable_A != self.Variable_B, "Los valores son distintos"

    def test_003(self):
        self.Variable_A = 15

        if self.Variable_A < 3:
            pytest.skip("El valor es muy inferior para ejecutar la prueba")

        if self.Variable_A >= 10:
            self.Resultado = True
        else:
            self.Resultado = False

        assert self.Resultado, f"El valor no es mayor es: {self.Variable_A}"

    def test_004(self):
        self.Variable_A = 10

        if self.Variable_A < 3:
            unittest.TestCase.skipTest("El valor es muy inferior para ejecutar la prueba")

        if self.Variable_A >= 10:
            self.Resultado = True
        else:
            self.Resultado = False

        assert self.Resultado, f"El valor no es mayor es: {self.Variable_A}"

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
