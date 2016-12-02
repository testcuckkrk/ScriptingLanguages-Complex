import unittest
from Complex import Complex

    class TestEq(unittest.TestCase):


	     def test_equal(self):
	    	c1 = Complex(7,11)
	       c2 = Complex(9,11)

			self.assertEqual(Complex.__eq__(c1), c2 )


	    if __name__ == '__main__':
unittest.main() 
