from Neurons import Perceptron
class Summing:

	def __init__(self):
		self.nand_gate = Perceptron([-2, -2], 3)
		self.sum = 0
		self.carry = 0

	def add(self, bit1, bit2):
		op1 = self.nand_gate.feed([bit1, bit2])
		op2 = self.nand_gate.feed([bit1, op1])
		op3 = self.nand_gate.feed([op1, bit2])
		self.sum = self.nand_gate.feed([op2, op3])
		self.carry = self.nand_gate.feed([op1, op1])


