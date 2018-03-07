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

def soma(m1, m2): #diferente da somarMatrizes esta funcao soma duas matrizes do mesmo tamanho
	tamanho = len(m1)
	aux = criarMatriz(tamanho)

	for i in range(0,tamanho):
		for j in range(0,tamanho):
			aux[i][j] = m1[i][j] + m2[i][j]

	return aux

def subtracao(m1, m2): #esta funcao subtrai duas matrizes do mesmo tamanho
	tamanho = len(m1)
	aux = criarMatriz(tamanho)

	for i in range(0,tamanho):
		for j in range(0,tamanho):
			aux[i][j] = m1[i][j] - m2[i][j]

	return aux

def multiplicar(matrizA, matrizB):
    tamanho = len(matrizA)
    auxiliarC = criarMatriz(tamanho)
    for i in range(0,tamanho):
        for k in range(0,tamanho):
            for j in range(0,tamanho):
                auxiliarC[i][j] += matrizA[i][k] * matrizB[k][j]
    return auxiliarC

def Strassen(matrizA , matrizB):
	# Coloque seu código aqui
	dimensao = len(matrizA)

	if(dimensao<=2):
		#caso base Strassen
		'''matrizC = criarMatriz(dimensao)
		#print(matrizA[0][0])

		p1 = matrizA[0][0] * (matrizB[0][1] - matrizB[1][1]) #p1=a(f-h)
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


		return matrizC'''
		#testando com multiplicacao simples tendo como embasamento a matriz ser pequena 2x2
		return multiplicar(matrizA, matrizB)
	else:
		#dividir as dimensoes por 2 e passar as matrizes para strassen
		dim_metade = dimensao//2
		#print(10//2)
		#print(dimensao)
		#print(dim_metade)

		#aplicando a lógica do Strassen porém cada espaço é uma matriz

		a11 = criarMatriz(dim_metade)
		a12 = criarMatriz(dim_metade)
		a21 = criarMatriz(dim_metade)
		a22 = criarMatriz(dim_metade)

		b11 = criarMatriz(dim_metade)
		b12 = criarMatriz(dim_metade)
		b21 = criarMatriz(dim_metade)
		b22 = criarMatriz(dim_metade)

		#matrizes auxiliares
		auxiliarA = criarMatriz(dim_metade)
		auxiliarB = criarMatriz(dim_metade)

		for i in range(0, dim_metade): #separando a matriz original em 4
			for j in range(0, dim_metade):
				a11[i][j] = matrizA[i][j]
				a12[i][j] = matrizA[i][j + dim_metade]
				a21[i][j] = matrizA[i + dim_metade][j]
				a22[i][j] = matrizA[i + dim_metade][j + dim_metade]

				b11[i][j] = matrizB[i][j]
				b12[i][j] = matrizB[i][j + dim_metade]
				b21[i][j] = matrizB[i + dim_metade][j]
				b22[i][j] = matrizB[i + dim_metade][j + dim_metade]
		
		#Strassen é aplicado recursivamente		
		auxiliarA = soma(a11,a22)
		auxiliarB = soma(b11,b22)
		p1 = Strassen(auxiliarA, auxiliarB)

		auxiliarA = soma(a21, a22)
		p2 = Strassen(auxiliarA, b11)

		auxiliarB = subtracao(b12,b22)
		p3 = Strassen(a11, auxiliarB)

		auxiliarB = subtracao(b21, b11)
		p4 = Strassen(a22, auxiliarB)

		auxiliarA = soma(a11, a12)
		p5 = Strassen(auxiliarA, b22)

		auxiliarA = subtracao(a21, a11)
		auxiliarB = soma(b11, b12)
		p6 = Strassen(auxiliarA, auxiliarB)

		auxiliarA = subtracao(a12, a22)
		auxiliarB = soma(b21, b22)
		p7 = Strassen(auxiliarA, auxiliarB)

		#calculando a matriz resultado

		c12 = soma(p3, p5)
		c21 = soma(p2, p4)

		auxiliarA = soma(p1, p4)
		auxiliarB = soma(auxiliarA, p7)
		c11 = subtracao(auxiliarB, p5)

		auxiliarA = soma(p1, p3)
		auxiliarB = soma(auxiliarA, p6)
		c22 = subtracao(auxiliarB, p2)

		#juntando os resultados em uma só matriz

		matrizC = criarMatriz(dimensao)

		for i in range(0, dim_metade):
			for j in range(0, dim_metade):
				matrizC[i][j] = c11[i][j]
				matrizC[i][j + dim_metade] = c12[i][j]
				matrizC[i + dim_metade][j] = c21[i][j]
				matrizC[i + dim_metade][j + dim_metade] = c22[i][j]

		return matrizC

m_dim_matrizes = 0
dim_final = 0

m1 , m2, lineM1, rowM1, lineM2, rowM2 = readFiles( 'M1.in' , 'M2.in' )

#print('As dimensões das matrizes são: ',lineM1, rowM1, lineM2, rowM2)

m_dim_matrizes = dimensaoDominante(lineM1, rowM1, lineM2, rowM2)

#print('A maior dimensão entre as matrizes é: ',m_dim_matrizes)

dim_final = dimensaoFinal(m_dim_matrizes)

#print('A dimensão final para aplicação do algoritmo Strassen será de: ', dim_final)


# ------------------------------------------------
matrizA = criarMatriz(dim_final)
matrizB = criarMatriz(dim_final)

somarMatrizes(m1, matrizA, lineM1, rowM1)
somarMatrizes(m2, matrizB, lineM2, rowM2)

matriz_resultado = Strassen(matrizA, matrizB)

#print(matriz_resultado)

#imprimindo no arquivo o resultado
file = open("M3.out", "w") 
for i in range(0,lineM1):
	for j in range(0, rowM2):
		file.write(str(matriz_resultado[i][j]))
		file.write(' ')
	file.write('\n')

file.close()
