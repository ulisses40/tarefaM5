import unittest
from fizzbuzz_utils import verificar_multiplo

class TestFizzBuzzUtils(unittest.TestCase):
    def test_multiplo_de_5(self):
        self.assertEqual(verificar_multiplo(10), "FIZZ")

    def test_multiplo_de_7(self):
        self.assertEqual(verificar_multiplo(14), "BUZZ")

    def test_multiplo_de_ambos(self):
        self.assertEqual(verificar_multiplo(35), "FIZZBUZZ")

    def test_nao_multiplo(self):
        self.assertEqual(verificar_multiplo(8), "MISS")

if __name__ == "__main__":
    unittest.main()
