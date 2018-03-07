a = [[1,2],[1,2],[2,3],[2,3]]
print(a)


'''aux = 0
for i in range(0,len(a)):
	#print(a[0][i])
	if a[0][i] != 0:
		aux = aux + 1
	else: 
		colunas = aux
		break


for i in range(0,len(a)):
	#print(a[0][i])
	if a[i][0] != 0:
		aux = aux + 1
	else: 
		linhas = aux
		break
'''
'''def linhas_matriz(matriz_resultado):
	linhas = 0
	print(matriz_resultado)
	for i in range(0,len(matriz_resultado)):
			if(matriz_resultado[i][0] != 0):
				linhas = linhas + 1
	return linhas


def colunas_matriz(matriz_resultado):
	colunas = 0
	print(matriz_resultado)
	for i in range(0,len(matriz_resultado)):
			if(matriz_resultado[0][i] != 0):
				colunas = colunas + 1
	return colunas

colunas = 0
linhas = 0
largura = len(a)-1

if(a[largura][largura] != 0):
	print(a)
else:

	linhas = linhas_matriz(a)
	colunas = colunas_matriz(a)

	for i in range(0,len(a)):
		if(a[i][0] != 0):
			linhas = linhas + 1

	for j in range(0, len(a)):
		if(a[0][j] != 0):
			colunas = colunas + 1



print('Colunas: ',colunas)
print('Linhas: ',linhas)


b = [[0 for x in range(0,colunas)] for x in range(0, linhas)]

print(b)

for i in range(0, linhas):
	for j in range(0, colunas):
		b[i][j] = a[i][j]

print(b)
'''

print(len(a[0]))
print(len(a))