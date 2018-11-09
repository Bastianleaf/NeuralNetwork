import unittest
from Neurons import Perceptron


class TestPerceptron(unittest.TestCase):
	
	def setUp(self):
		self.perceptron = Perceptron([1, 2, 3], -3)
		self.and_gate = Perceptron([2, 2], -3)
		self.or_gate = Perceptron([4, 4], -3)
		self.nand_gate = Perceptron([-2, -2], 3)
		self.nor_gate = Perceptron([-2, -2], 1)

	def test_feed(self):
		self.assertEqual(self.perceptron.feed([0, 0, 0]), 0, 'Error caso < 0')
		self.assertEqual(self.perceptron.feed([0, 0, 2]), 1, 'Error caso > 0')
		self.assertEqual(self.perceptron.feed([2, -3, 6]), 1, '')

	def test_and(self):
		self.assertEqual(self.and_gate.feed([0,0]), 0, 'Error caso 0 0')
		self.assertEqual(self.and_gate.feed([0,1]), 0, 'Error caso 0 1')
		self.assertEqual(self.and_gate.feed([1,0]), 0, 'Error caso 1 0')
		self.assertEqual(self.and_gate.feed([1,1]), 1, 'Error caso 1 1')

	def test_or(self):
		self.assertEqual(self.or_gate.feed([0,0]), 0, 'Error caso 0 0')
		self.assertEqual(self.or_gate.feed([0,1]), 1, 'Error caso 0 1')
		self.assertEqual(self.or_gate.feed([1,0]), 1, 'Error caso 1 0')
		self.assertEqual(self.or_gate.feed([1,1]), 1, 'Error caso 1 1')	

	def test_nand(self):
		self.assertEqual(self.nand_gate.feed([0,0]), 1, 'Error caso 0 0')
		self.assertEqual(self.nand_gate.feed([0,1]), 1, 'Error caso 0 1')
		self.assertEqual(self.nand_gate.feed([1,0]), 1, 'Error caso 1 0')
		self.assertEqual(self.nand_gate.feed([1,1]), 0, 'Error caso 1 1')

	def test_nor(self):
		self.assertEqual(self.nor_gate.feed([0,0]), 1, 'Error caso 0 0')
		self.assertEqual(self.nor_gate.feed([0,1]), 0, 'Error caso 0 1')
		self.assertEqual(self.nor_gate.feed([1,0]), 0, 'Error caso 1 0')
		self.assertEqual(self.nor_gate.feed([1,1]), 0, 'Error caso 1 1')



if __name__ == '__main__':
    unittest.main()