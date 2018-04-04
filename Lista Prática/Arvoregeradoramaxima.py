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



vertexs = ['A', 'B', 'C', 'D']
edges = [
    (1, 'A', 'B'),
    (5, 'A', 'C'),
    (3, 'A', 'D'),
    (4, 'B', 'C'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
]

print(kruskal(vertexs, edges))
