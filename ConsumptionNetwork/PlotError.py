import matplotlib.pyplot as plt

error_array = []
output = "../dataset/output_deseado.data" #output deseado
outputs_array = [0, 1, 10, 50, 100, 500, 1000] #outputs generados
with open(output, 'r') as g:
	for n in outputs_array:
		error_list = []
		with open("../dataset/output_adquirido_" + str(n) + ".data", 'r+') as f:
			for (line_d, line_o) in zip(f.readlines(), g.readlines()):
				data_line = line_d.rstrip().split(",")
				output_line = line_o.rstrip().split(",")

				error_inputs = (list(map(lambda x, y: (float(x) - float(y)) ** 2, output_line, data_line)))
				error_sum = sum(error_inputs)
				error_list.append(error_sum)
			g.seek(0)
			prom_outputs = (list(map(lambda x: x / 19, error_list)))
			error_prom = sum(prom_outputs) /377
			#print(prom_outputs)
			#print(error_prom)
			error_array.append(error_prom)
		f.close()
	g.close()
error_array = (list(map(lambda x: 1 - x, error_array)))
plt.plot([0, 1, 10, 50, 100, 500, 1000], error_array)
plt.axis([0, 20, 0.5, 1])
plt.ylabel('Precisión')
plt.xlabel('Cantidad de Entrenamiento')
plt.show()