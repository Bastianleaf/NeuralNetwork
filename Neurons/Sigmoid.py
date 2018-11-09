import Neurons
import numpy


class Sigmoid(Neurons.AbstractNeuron):

	def __init__(self, weight, bias):
		super().__init__(weight, bias)

	def evaluate(self, output):
		return 1.0 / (1.0 + numpy.exp(-output))


