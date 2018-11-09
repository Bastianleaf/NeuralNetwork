import unittest
from Summing import Summing


class TestPerceptron(unittest.TestCase):
	
	def setUp(self):
		self.bit1 = 0
		self.bit2 = 1
		self.summing = Summing()  

	def test_sum00(self):
		self.summing.add(self.bit1, self.bit1)
		self.assertEqual(self.summing.sum, 0, 'Error suma caso 0 + 0')
		self.assertEqual(self.summing.carry, 0, 'Error carry caso 0 + 0')

	def test_sum01(self):
		self.summing.add(self.bit1, self.bit2)
		self.assertEqual(self.summing.sum, 1, 'Error suma caso 0 + 1')
		self.assertEqual(self.summing.carry, 0, 'Error carry caso 0 + 1')

	def test_sum10(self):
		self.summing.add(self.bit2, self.bit1)
		self.assertEqual(self.summing.sum, 1, 'Error suma caso 1 + 0')
		self.assertEqual(self.summing.carry, 0, 'Error carry caso 1 + 0')

	def test_sum11(self):
		self.summing.add(self.bit2, self.bit2)
		self.assertEqual(self.summing.sum, 0, 'Error suma caso 1 + 1')
		self.assertEqual(self.summing.carry, 1, 'Error carry caso 1 + 1')


if __name__ == '__main__':
	unittest.main()
