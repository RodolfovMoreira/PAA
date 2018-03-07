def criarMatriz(tamanho): #cria uma matriz de 0's nxn sendo n a potencia de 2 seguinte a maior dimensao das matrizes

	matriz = [[0 for x in range(0,tamanho)] for x in range(0,tamanho)] 

	return matriz

def somarMatrizes(m1 , m2, lineM1, rowM1): #soma as matrizes a dimensão dada é da menor matriz
	for y in range(0,lineM1):
		for x in range(0,rowM1):
			m2[y][x] = m1[y][x] + m2[y][x]

def dimensaoFinal(m_dim_matrizes):  #acha qual o multiplo de 2 seguinte a maior dimensão

	dim_final = 1

	while(dim_final < m_dim_matrizes):
		dim_final = dim_final<<1

	return dim_final

def dimensaoDominante(lineM1, rowM1, lineM2, rowM2): #define qual a maior dimensão entre linhas/colunas

	maior_linha = 0
	maior_coluna = 0

	if(lineM1 > lineM2):
		maior_linha = lineM1
	else: 
		maior_linha = lineM2 

	if(rowM1 > rowM2):
		maior_coluna = rowM1
	else:
		maior_coluna = rowM2

	if(maior_coluna > maior_linha):
		return maior_coluna
	else:
		return maior_linha

def readFiles( name_m1 , name_m2 ):

	matrix1 = []
	matrix2 = []

	readM1 = open(name_m1, 'r')
	lineM1, rowM1 = map( int, readM1.readline().split() )
	for i in range(lineM1):
		matrix1 += 	[list(map( int, readM1.readline().split() ))]

	readM2 = open(name_m2, 'r')
	lineM2, rowM2 = map( int, readM2.readline().split() )
	for i in range(lineM2):
		matrix2 += 	[list(map( int, readM2.readline().split() ))]

	readM2.close()
	readM1.close()

	return matrix1, matrix2, lineM1, rowM1, lineM2, rowM2

def Strassen( matrizA , matrizB, dimensao):
	# Coloque seu código aqui
	if(dimensao<=2):
		#caso base Strassen
		p1 = matrizA[0[0]] * (matrizB[0][1] - matrizB[1][1]) #p1=a(f-h)
		p2 = (matrizA[0][0] + matrizA[0][1]) * matrizB[1][1] #p2=(a+b)h
		p3 = (matrizA[1][0] + matrizA[1][1]) * matrizB[0][0] #p3=(c+d)e
		p4 = matrizA[1][1] * (matrizB[1][0] - matrizB[0][0]) #p4=d(g-e)
		p5 = (matrizA[0][0] + matrizA[1][1]) * (matrizB[0][0] + matrizB[1][1]) #p5=(a+d)(e+h)
		p6 = (matrizA[0][1] - matrizA[1][1]) * (matrizB[1][0] + matrizB[1][1]) #p6=(b-d)(g+h)
		p7 = (matrizA[0][0] - matrizA[1][0]) * (matrizB[0][0] + matrizB[0][1]) #p7=(a-c)(e+f)

		matrizC[0][0] = p5+p4-p2+p6
		matrizC[0][1] = p1+p2
		matrizC[1][0] = p3+p4
		matrizC[0][1] = p1+p5-p3-p7

		return matrizC
	else:
		#dividir as dimensoes por 2 e passar as matrizes para strassen
		

	pass

m_dim_matrizes = 0
dim_final = 0

m1 , m2, lineM1, rowM1, lineM2, rowM2 = readFiles( 'M1.in' , 'M2.in' )

print('As dimensões das matrizes são: ',lineM1, rowM1, lineM2, rowM2)

m_dim_matrizes = dimensaoDominante(lineM1, rowM1, lineM2, rowM2)

print('A maior dimensão entre as matrizes é: ',m_dim_matrizes)

dim_final = dimensaoFinal(m_dim_matrizes)

print('A dimensão final para aplicação do algoritmo Strassen será de: ', dim_final)


# ------------------------------------------------
matrizA = criarMatriz(dim_final)
matrizB = criarMatriz(dim_final)

somarMatrizes(m1, matrizA, lineM1, rowM1)
somarMatrizes(m2, matrizB, lineM2, rowM2)

print(matrizA)
print(matrizB)

