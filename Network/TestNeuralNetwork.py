import unittest
import Network


class TestNeuralNetwork(unittest.TestCase):
	def setUp(self):
		l1 = Network.NeuralLayer(1, 2, "sigmoid")
		l2 = Network.NeuralLayer(1, 2, "sigmoid")
		for neuron in l1.neurons:
			neuron.bias = 0.5
			neuron.weight = [0.4, 0.3]
		for neuron in l2.neurons:
			neuron.bias = 0.4
			neuron.weight = [0.3]
		self.neural_network = Network.NeuralNetwork([l1, l2])
		self.neural_network.train([1, 1], [1], 0.5)
	
	def test_bias_first_neuron(self):
		self.assertEqual(self.neural_network.first_layer.neurons[0].bias, 0.502101508999489)
		
	def test_weight_first_neuron(self):
		self.assertEqual(self.neural_network.first_layer.neurons[0].weight, [0.40210150899948904, 0.302101508999489])
	
	def test_bias_second_neuron(self):
		self.assertEqual(self.neural_network.first_layer.next_layer.neurons[0].bias, 0.43937745312797394)

	def test_weight_second_neuron(self):
		self.assertEqual(self.neural_network.first_layer.next_layer.neurons[0].weight, [0.33026254863991883])

