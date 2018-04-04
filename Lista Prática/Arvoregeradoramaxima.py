"""vertexs = ['A', 'B', 'C', 'D']
edges = [
    (1, 'A', 'B'),
    (5, 'A', 'C'),
    (3, 'A', 'D'),
    (4, 'B', 'C'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
]

print(kruskal(vertexs, edges))"""

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

    edges.sort(reverse = True) #Sort em ordem decrescente (Maximum Spanning Tree)
    
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst.append(edge)
    return mst

def lendo_ABC():
	A,B,C = [int(i) for i in input().split()]
	lis_aux = (C, A, B)
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
	mst = kruskal(vertices, edges)
	#print(mst)

	for vertices in mst:
		soma = soma + vertices[0]

	print(soma)



n_casos = int(input())
i = 0

while i != n_casos:
	magica()
	i = i+1