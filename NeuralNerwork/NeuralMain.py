from NeuralLayer import NeuronLayer
from NeuralNetwork import NeuralNetwork
from Perceptron import Perceptron
from Sigmoid import Sigmoid
import random


def layer(n, weight_lenght, type):
	neurons = []
	for i in range(n):
		weight = []
		bias = random.uniform(-2, 2)
		for w in range(weight_lenght):
			weight.append(random.uniform(-2, 2))
		if type == "sigmoid":
			neuron = Sigmoid(weight, bias)
		else:
			neuron = Perceptron(weight, bias)
		neurons.append(neuron)
	return NeuronLayer(neurons)

#Aprender XOR
layer_a = layer(3, 2, "sigmoid")
layer_b = layer(1, 3, "sigmoid")
network = NeuralNetwork([layer_a, layer_b])
for i in range(0, 10000):
	# aprender 0 - 0 -> 0
	output = network.feed([0, 0])
	expected_output = [0]
	network.backward_propagate_error(expected_output)
	network.update_weight([0, 0])

	#aprender 0 - 1 -> 1
	output = network.feed([0, 1])
	expected_output = [1]
	network.backward_propagate_error(expected_output)
	network.update_weight([0, 1])

	#aprender 1 - 0 -> 1
	output = network.feed([1, 0])
	expected_output = [1]
	network.backward_propagate_error(expected_output)
	network.update_weight([1, 0])

	#aprender 1 - 1 -> 1
	output = network.feed([1, 1])
	expected_output = [0]
	network.backward_propagate_error(expected_output)
	network.update_weight([1, 1])

print(network.feed([0, 0]))
print(network.feed([1, 0]))
print(network.feed([0, 1]))
print(network.feed([1, 1]))


