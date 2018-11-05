import numpy as np

class NeuralNetwork:

	def __init__(self, layers):
		self.first_layer = layers[0]
		self.last_layer = layers[len(layers) - 1]
		self.outputs = []
		
		if len(layers) != 1:
			layers[0].set_next_layer(layers[1])
			for i in range(1, len(layers) - 2):
				layers[i].set_previous_layer(layers[i - 1])
				layers[i].set_next_layer(layers[i + 1])
			layers[len(layers) - 1].set_previous_layer(layers[len(layers) - 2])
			
	def train(self, inputs, desired_output):
		self.outputs = self.feed(inputs)

	def feed(self, inputs):
		output = self.first_layer.feed(inputs)
		layer = self.first_layer.next_layer
		while layer is not None:
			output = layer.feed(output)
			layer = layer.next_layer
		return output
	
	def backward_propagate_error(self, expected_outputs):
		self.last_layer.backward_propagate_error(expected_outputs)
		

	def update_weight(self, inputs):
		self.first_layer.update_weight(inputs)