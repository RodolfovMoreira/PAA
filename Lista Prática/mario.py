#MARIO

#http://www.thehuxley.com/problem/646?quizId=2687

def binarySearch(lista, item):
	aux = 0
	first = 0
	last = len(lista)-1

	while first<=last:
		midpoint = (first+last)//2
		if lista[midpoint] == item:
			return midpoint,midpoint
		else:
			if item < lista[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
	return False,midpoint

midpoint = 0
passou = 0
N,L = [int(i) for i in input().split()]

while (N!= 0)&(L!=0):
	if(N == 1 and L >= N):
		armarios = [int(i) for i in input().split()]
		print(0)
	else:
		melhor = L
		armarios = [int(i) for i in input().split()]
		for i in range(0,len(armarios)-1):
			elemento = armarios[i]
			elemento = elemento + N - 1
			posicao,midpoint = binarySearch(armarios,elemento)
			if(posicao == False):
				passou = 1
				if(armarios[midpoint] < elemento):
					midpoint = midpoint + 1
			posicao = midpoint
			if(posicao != False):
				if(passou != 1):
					armarios_livres = posicao - i + 1
				else:
					armarios_livres = posicao - i
				passou = 0
				trocas = N - armarios_livres
				if(trocas < melhor):
					melhor = trocas
		print(melhor)
	
	N,L = [int(i) for i in input().split()]

