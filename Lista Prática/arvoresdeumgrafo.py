
parent = dict()
rank = dict()


def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex]) 
    return parent[vertex]

def union(v1, v2):
    raiz1 = find(v1)
    raiz2 = find(v2)
    
    if raiz1 == raiz2: return
    
    if raiz1 < raiz2:
        parent[raiz1] = raiz2
    elif raiz1 > raiz2:
        parent[raiz2] = raiz1
    else:
        parent[raiz2] = raiz1
        rank[raiz1] += 1

def kruskal(v, edges):
    mst = []
    for vertices in v:
        make_set(vertices)

    edges.sort() #Sort em ordem crescente (Minimum Spanning Tree)
    
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst.append(edge)
    return mst

def lendo_ABC():
	A,B,C = [int(i) for i in input().split()]
	lis_aux = (C, A+1, B+1)
	return(lis_aux)

def magica(): #Roda oque é pedido para cada teste
	i = 0
	soma = 0
	edges = []
	vertices = []
	n,m = [int(i) for i in input().split()]

	while i != m:
		edges.append(lendo_ABC())
		i = i+1
	i = 1
	while i != n+1:
		vertices.append(i)
		i = i+1
	
	#print(vertices)
	return(n,m,vertices,edges)


def soma_mst(mst):
    soma = 0
    for vertices in mst:
        soma = soma+vertices[0]
    return soma

def copy(x):
    return x

def reeniciate(): #ARRUMANDO AS GLOBAIS
    global parent
    global rank
    parent = dict()
    rank = dict()

def voltazero():
    return 0

soma = float("inf")
somaorigi = 0
aux = 0
mst2 = 0
n,m,vertices,edges = magica()
#print(edges)
edges_copia = copy(edges)
mst = kruskal(vertices,edges)
somaorigi = soma_mst(mst)
reeniciate()
#print(mst)
#print(soma_mst(mst))
#print(edges_copia)
#print('-----------------------------')
for aresta in mst:
    #print(aresta)
    #print(edges_copia)
    edges_copia.remove(aresta)
    #print(edges_copia)
    mst2 = kruskal(vertices,edges_copia)
    reeniciate()
    edges_copia.append(aresta)
    if(len(mst2)==len(mst)):
        aux = soma_mst(mst2)
        if(aux < soma):
            if(aux != somaorigi):
                soma = aux
    mst2 = voltazero()
    #soma = soma_mst(mst2)
    #print(soma)
    #edges_copia = copy(edges)
#print(soma)
print('First Spanning Tree Cost:',somaorigi)
print('Second Spanning Tree Cost:',soma)
