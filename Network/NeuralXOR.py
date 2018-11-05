import Network
import random

# aprender XOR


layer_a = Network.NeuralLayer(3, 2, "sigmoid")
layer_b = Network.NeuralLayer(1, 3, "sigmoid")
network = Network.NeuralNetwork([layer_a, layer_b])
for i in range(0, 10000):
	# aprender 0 - 0 -> 0
	network.train([0, 0], [0])
	
	#aprender 0 - 1 -> 1
	network.train([0, 1], [1])

	#aprender 1 - 0 -> 1
	network.train([1, 0], [1])
	
	#aprender 1 - 1 -> 1
	network.train([1, 1], [0])
	
print(network.feed([0, 0]))
print(network.feed([1, 0]))
print(network.feed([0, 1]))
print(network.feed([1, 1]))


