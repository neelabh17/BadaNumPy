import unittest
from CoinChangeIterDP import coinChangeI
from CionChangeRecur import coinChangeR
class NamesTestCase(unittest.TestCase):
	def test_first_last_name1(self):
		formatted_name =  coinChangeR(1,5)
		self.assertEqual(formatted_name,coinChangeI(1,5))



unittest.main()
