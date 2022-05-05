import unittest

class test_002 (unittest.TestCase): # llamamos a la libreria para evaluar los resultados

    def setUp(self):
        pass

    def test_002(self):
        self.Variable_A = 50
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertEqual(self.Variable_A, self.Variable_B, "Los valores son iguales")

    def test_003(self):
        self.Variable_A = 50
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertEqual(self.Variable_A, self.Variable_B, "Los valores son distintos") # validaciones de la libreria de Unittest

    def test_004(self):
        self.Variable_A = 60
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B, "Los valores no son iguales"

        self.assertNotEqual(self.Variable_A, self.Variable_B, "Los valores no son iguales")

    def test_005(self):
        self.Variable_A = "Libreria de Unittest"
        self.Variable_B = "Unittest"

        self.assertIn(self.Variable_B, self.Variable_A, f"No coinciden") # assertIn valida que " a in b" = a este incluido en b







    def tearDown(self):
        pass

    # constructor:
    if __name__ == '__main__':
        unittest.main()