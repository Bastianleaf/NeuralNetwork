lines =[]
with open('a') as f:
	for line in f:
		a = line.split(" ")
		if len(a) > 9:
			lines.append([a[6], a[8]])
		if len(a) > 7:
			lines.append([a[3], a[5]])
		lines.append([a[0], a[2]])
lines.sort()
f.close()
with open('b', 'w') as g:
	for line in lines:
		print(line)
		g.write(line[0] + ' & ' + line[1] + ' \\' + '\\ \hline' +'\n')
		
g.close()