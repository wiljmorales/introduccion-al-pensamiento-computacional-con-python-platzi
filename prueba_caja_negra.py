import unittest

def suma(num_1, num_2):
  return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

  def test_suma_dos_positivos(self):
    num_1 = 10
    num_2 = 4

    resultado = suma(num_1, num_2)

    self.assertEqual(resultado, 14)

  def test_suma_dos_negativos(self):
    self.assertEqual(suma(-2, -3), -5)

if __name__ == "__main__":
  unittest.main()