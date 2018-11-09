import Neurons

class Perceptron(Neurons.AbstractNeuron):

	def __init__(self, weight, bias):
		super().__init__(weight, bias)

	def evaluate(self, output):
		if output > 0:
			return 1
		else:
			return 0


