import unittest


class test_001(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        self.Variable_A = 50
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertTrue(self.RESULTADO >= 100, f"El valor no es 10")

    def test_002(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Debería ser 6")


    def tearDown(self):
        pass


class test_002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'Mervin '
        self.Variable_B = 'Alberto'

    def test_comparacion(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self):
        self.assertEqual("Mervin Alberto", self.RESULTADO, f"El resultado es diferente al esperado: {self.RESULTADO}")

if __name__ == '__main__':
    unittest.main()
