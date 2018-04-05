#MARIO

#http://www.thehuxley.com/problem/646?quizId=2687

def binarySearch(lista, item):
	first = 0
	last = len(lista)-1

	while first<=last:
		midpoint = (first+last)//2
		if lista[midpoint] == item:
			return midpoint
		else:
			if item < lista[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
	return False


N,L = [int(i) for i in input().split()]

while (N!= 0)&(L!=0):
	melhor = L
	armarios = [int(i) for i in input().split()]
	for i in range(0,len(armarios)-1):
		elemento = armarios[i]
		elemento = elemento + N - 1
		posicao = binarySearch(armarios,elemento)
		#print(posicao,'posicao',elemento)
		if(posicao != False):
			armarios_livres = posicao - i + 1
			trocas = N - armarios_livres
			if(trocas < melhor):
				melhor = trocas
	print(melhor)
	N,L = [int(i) for i in input().split()]

