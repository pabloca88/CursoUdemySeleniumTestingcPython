import unittest

class test_002 (unittest.TestCase): # llamamos a la libreria para evaluar los resultados

    def setUp(self):
        pass

    def test_002(self):
        self.Variable_A = 50
        self.Variable_B = 51
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertEqual(self.Variable_A, self.Variable_B, "Los valores son distintos")



    def tearDown(self):
        pass

    # constructor:
    if __name__ == '__main__':
        unittest.main()