import Network

layer_a = Network.NeuralLayer(5, 12, "sigmoid")
layer_b = Network.NeuralLayer(19, 5, "sigmoid")
network = Network.NeuralNetwork([layer_a, layer_b])
# cantidad de entrenamiento
for n in [0, 10, 50, 100, 500, 1000, 5000, 10000]:
	for i in range(n):
		with open('../dataset/data_normalizada.data', 'r+') as f:
			for line in f.readlines():
				line = line.rstrip().split(",")
				inputs = list(map(float, line[:13]))
				output = list(map(float, line[14:]))
				network.train(inputs, output)
		f.close()
	
	with open('../dataset/data_normalizada.data', 'r+') as f:
		with open('../dataset/output_adquirido_' + str(n) + '.data', 'w+') as h:
			for line in f.readlines():
				test_line = line.rstrip().split(",")
				test_inputs = list(map(float, test_line[:13]))
				h.write(",".join((map(str, network.feed(test_inputs)))) + '\n')
	f.close()
	h.close()