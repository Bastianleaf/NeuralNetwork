class AbstractNeuron:
	
	def __init__(self, weight, bias):
		self.weight = weight
		self.bias = bias
		self.output = 0
		self.delta = 0
		
	def feed(self, inp):
		res = 0.0
		for x in range(0, len(self.weight)):
			res = res + inp[x] * self.weight[x]
		output = res + self.bias
		self.output = self.evaluate(output)
		return self.output
	
	def evaluate(self, output):
		pass
	
	def adjust_delta_with(self, error):
		self.delta = error * (self.output * (1.0 - self.output))

	def set_weight(self, weight):
		self.weight = weight
		
	def set_bias(self, bias):
		self.bias = bias
		
	def get_weight(self):
		return self.weight
	
	def get_bias(self):
		return self.bias
	
	def get_output(self):
		return self.output
	
	def adjust_bias_using_learning_rate(self, learning_rate):
		self.bias = self.bias + (learning_rate * self.delta)
		
	def adjust_weight_with_input(self, inputs, learning_rate):
		for i in range(len(self.weight)):
			self.weight[i] = self.weight[i] + (learning_rate * self.delta * inputs[i])
	
	def get_delta(self):
		return self.delta
