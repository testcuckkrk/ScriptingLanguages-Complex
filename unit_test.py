import unittest 
from Complex import Complex

class TestReal(unittest.TestCase):	

	
	def test_real(self):
		c1 = Complex(7,11) 
		self.assertEqual(Complex.real(c1), 7)


if __name__ == '__main__':
	unittest.main()
