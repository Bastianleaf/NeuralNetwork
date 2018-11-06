lines =[]
with open('a') as f:
	for line in f:
		a = line.split(" ")
		if len(a) > 7:
			lines.append([a[6], a[8]])
		if len(a) > 4:
			lines.append([a[3], a[5]])
		lines.append([a[0], a[1]])
lines.sort()
f.close()
with open('b', 'w') as g:
	for line in lines:
		g.write(line[1] + ' & ' + line[0] + ' \\' + '\\ \hline' +'\n')
		
g.close()