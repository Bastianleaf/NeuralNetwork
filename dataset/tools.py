def normalizar(min, max):
	return lambda x: (x - min)/(max - min)


edad = normalizar(-0.95197, 2.59171)
genero = normalizar(-0.48246, 0.48246)
educacion = normalizar(-2.43591, 1.98437)
pais = normalizar(-0.57009, 0.96082)
etnia = normalizar(-1.10702, 1.90725)
n_score = normalizar(-3.46436, 3.27393)
e_score = normalizar(-3.27393, 3.27393)
o_score = normalizar(-3.27393, 2.90161)
a_score = normalizar(-3.46436, 3.46436)
c_score = normalizar(-3.46436, 3.46436)
impulsive = normalizar(-2.55524, 2.90161)
SS = normalizar(-2.07848, 1.92173)
outputs = normalizar(0, 6)

outDict={
	"CL0": 0.0,
	"CL1": 0.16666,
	"CL2": 0.33333,
	"CL3": 0.5,
	"CL4": 0.66666,
	"CL5": 0.83333,
	"CL6": 1.0
	
}

with open("drug_consumption.data", "r") as fp:
	with open("data_normalizada.data", "w") as gp:
		for line in fp:
			linea = line.split(",")
			print(linea)
			linea[1] = edad(float(linea[1]))
			linea[2] = genero(float(linea[2]))
			linea[3] = educacion(float(linea[3]))
			linea[4] = pais(float(linea[4]))
			linea[5] = etnia(float(linea[5]))
			linea[6] = n_score(float(linea[6]))
			linea[7] = e_score(float(linea[7]))
			linea[8] = o_score(float(linea[8]))
			linea[9] = a_score(float(linea[9]))
			linea[10] = c_score(float(linea[10]))
			linea[11] = impulsive(float(linea[11]))
			linea[12] = SS(float(linea[12]))
			linea[13] = outDict[linea[13]]
			linea[14] = outDict[linea[14]]
			linea[15] = outDict[linea[15]]
			linea[16] = outDict[linea[16]]
			linea[17] = outDict[linea[17]]
			linea[18] = outDict[linea[18]]
			linea[19] = outDict[linea[19]]
			linea[20] = outDict[linea[20]]
			linea[21] = outDict[linea[21]]
			linea[22] = outDict[linea[22]]
			linea[23] = outDict[linea[23]]
			linea[24] = outDict[linea[24]]
			linea[25] = outDict[linea[25]]
			linea[26] = outDict[linea[26]]
			linea[27] = outDict[linea[27]]
			linea[28] = outDict[linea[28]]
			linea[29] = outDict[linea[29]]
			linea[30] = outDict[linea[30]]
			linea[31] = outDict[linea[31][:3]]
			toPrint = ",".join((map(str, linea)))
			gp.write(toPrint + '\n')
fp.close()
gp.close()
