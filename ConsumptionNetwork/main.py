import Network
from time import time

training_list = [5000, 10000] # crear arreglo con la cantidad de entrenamientos
layer_a = Network.NeuralLayer(5, 12, "sigmoid")  # un hidden layer: cantidad de neuronas, cantidad de input, tipo de neurona
layer_b = Network.NeuralLayer(19, 5, "sigmoid")
network = Network.NeuralNetwork([layer_a, layer_b]) # crear red
# cantidad de entrenamiento
# n -> array de cantidad de veces que se entrena
lr = 0.25 # definir learning rate

for n in training_list:
	#se abre el dataset y se entrena n veces
	
	with open('../dataset/data_normalizada.data', 'r+') as f:
		start_time = time()
		for i in range(n):
			for line in f.readlines():
				line = line.rstrip().split(",")
				inputs = list(map(float, line[:13]))
				output = list(map(float, line[14:]))
				network.train(inputs, output, lr)
			f.seek(0)
		elapsed_time = time() - start_time
	f.close()
	
	print("Tiempo con " + str(n) + " entrenamientos : %.10f segundos." % elapsed_time)
	#se escribe una archivo data con los output adquirido
	with open('../dataset/data_normalizada.data', 'r+') as f:
		with open('../dataset/output_adquirido_' + str(n) + '.data', 'w+') as h:
			for line in f.readlines():
				test_line = line.rstrip().split(",")
				test_inputs = list(map(float, test_line[:13]))
				h.write(",".join((map(str, network.feed(test_inputs)))) + '\n')
	f.close()
	h.close()