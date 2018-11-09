import unittest
import Network


class TestNeuralNetwork2(unittest.TestCase):
	def setUp(self):
		l1 = Network.NeuralLayer(2, 2, "sigmoid")
		l2 = Network.NeuralLayer(2, 2, "sigmoid")
		l1.neurons[0].bias = 0.5
		l1.neurons[0].weight = [0.7, 0.3]
		l1.neurons[1].bias = 0.4
		l1.neurons[1].weight = [0.3, 0.7]
		l2.neurons[0].bias = 0.3
		l2.neurons[0].weight = [0.2, 0.3]
		l2.neurons[1].bias = 0.6
		l2.neurons[1].weight = [0.4, 0.2]
		
		self.neural_network = Network.NeuralNetwork([l1, l2])
		self.neural_network.train([1, 1], [1, 1], 0.5)
	
	def test_bias_first_layer_first_neuron(self):
		self.assertEqual(self.neural_network.first_layer.neurons[0].bias, 0.5025104485493278)
	
	def test_weight_first_layer_first_neuron(self):
		self.assertEqual(self.neural_network.first_layer.neurons[0].weight, [0.7025104485493278, 0.3025104485493278])
	
	def test_bias_first_layer_second_neuron(self):
		self.assertEqual(self.neural_network.first_layer.neurons[1].bias, 0.40249801135748337)
	
	def test_weight_first_layer_second_neuron(self):
		self.assertEqual(self.neural_network.first_layer.neurons[1].weight, [0.30249801135748333, 0.7024980113574834])
	
	def test_bias_second_layer_first_neuron(self):
		self.assertEqual(self.neural_network.first_layer.next_layer.neurons[0].bias, 0.3366295422515899)
	
	def test_weight_second_layer_first_neuron(self):
		self.assertEqual(self.neural_network.first_layer.next_layer.neurons[0].weight, [0.22994737881955657, 0.32938362863950127])
		
	def test_bias_second_layer_second_neuron(self):
		self.assertEqual(self.neural_network.first_layer.next_layer.neurons[1].bias, 0.6237654881509048)

	def test_weight_second_layer_second_neuron(self):
		self.assertEqual(self.neural_network.first_layer.next_layer.neurons[1].weight, [0.41943005652646226, 0.21906429169838573])


