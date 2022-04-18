import unittest


class test_001(unittest.TestCase):

    def setUp(self):         #definimos los datos de prueba
        self.Variable_A = 6
        self.Variable_B = 4

    def test_001(self):      #definimos la prueba en si

        self.RESULTADO = self.Variable_A + self.Variable_B

    def TearDown(self):     #donde se evalua o se finaliza la prueba
        self.assertTrue(self.RESULTADO == 10, f"El valor no es 10, es (self.RESULTADO)")

class test_002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = "Pablo"
        self.Variable_B = "Martin"

    def test_002(self):
        self.RESULTADO = self.Variable_A + self.Variable_B

    def TearDown(self):
        self.assertEqual("Pablo Martin", self.RESULTADO, f"El resultado es diferente al esperado: (self.RESULTADO)")



if __name__ == '__main__':
    unittest.main()
