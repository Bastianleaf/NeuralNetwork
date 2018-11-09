import random
import Neuron


class NeuralLayer:
	
	def __init__(self, n, weight_lenght, type):
		neurons = []
		for i in range(n):
			weight = []
			bias = random.uniform(-2, 2)
			for w in range(weight_lenght):
				weight.append(random.uniform(-2, 2))
			if type == "sigmoid":
				neuron = Neuron.Sigmoid(weight, bias)
			else:
				neuron = Neuron.Perceptron(weight, bias)
			neurons.append(neuron)
		self.neurons = neurons
		self.next_layer = None
		self.previous_layer = None
		
	def feed(self, inputs):
		output = []
		for neuron in self.neurons:
			res = neuron.feed(inputs)
			output.append(res)
		return output
	
	def collect_outputs(self):
		outputs = []
		for neuron in self.neurons:
			outputs.append(neuron.get_output())
		return outputs
	
	def set_next_layer(self, next_layer):
		self.next_layer = next_layer
	
	def set_previous_layer(self, previous_layer):
		self.previous_layer = previous_layer
		
	def backward_propagate_error(self, expected_outputs):
		
		if self.next_layer is None:  # si es ultimo layer
			
			for i in range(len(expected_outputs)):
				error = expected_outputs[i] - self.neurons[i].output
				self.neurons[i].adjust_delta_with(error)

		else:  # si es un hidden layer
			for i in range(len(self.neurons)):
				error = 0.0
				for next_neuron in self.next_layer.neurons:
					error = error + next_neuron.weight[i] * next_neuron.delta
				self.neurons[i].adjust_delta_with(error)
				
		if self.previous_layer is not None:  # si no es primer layer, continua
			self.previous_layer.backward_propagate_error([])
			
	def update_weight(self, inputs, lr):
		learning_rate = lr
		if self.previous_layer is None:
			inputs = inputs
		else:
			inputs = self.previous_layer.collect_outputs()
		for neuron in self.neurons:
			neuron.adjust_weight_with_input(inputs, learning_rate)
			neuron.adjust_bias_using_learning_rate(learning_rate)
		if self.next_layer is not None:
			self.next_layer.update_weight(inputs, lr)

	def get_errors(self):
		deltas = []
		for neuron in self.neurons:
			deltas.append(neuron.delta)
		return deltas
	
	def get_outputs(self):
		outputs = []
		for neuron in self.neurons:
			outputs.append(neuron.output)
		return outputs
	
	def get_weights(self):
		weights = []
		for neuron in self.neurons:
			weights.append(neuron.weight)
		return weights
	
	def get_bias(self):
		bias = []
		for neuron in self.neurons:
			bias.append(neuron.bias)
		return bias
