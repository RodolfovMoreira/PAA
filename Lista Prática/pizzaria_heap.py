
import sys
from heapq import heappush, heappop

class Dijkstra:
    def __init__(self, adjacents):
        self.adj = adjacents
        self.n = len(adjacents)

    def dijkstra(self, start):
        dis, vis, hq = {}, {}, []

        for node in self.adj.keys():
            dis[node] = float('inf')
            vis[node] = False

        dis[start], vis[start] = 0, True
        heappush(hq, (0, start))

        while hq:
            (d, node) = heappop(hq)
            vis[node] = True

            for n, weight in self.adj[node].items():
                if (not vis[n]) and (d + weight < dis[n]):
                    dis[n] = d + weight
                    heappush(hq, (dis[n], n))

        return dis


def make_reciprocity(graph,v,u):
    graph[u][v] = graph[v][u]

def check_reciprocity(graph,v,u):
    if graph[u].get(v) == None:
        make_reciprocity(graph,v,u)

def lendo_ABC():
  A,B,C = [int(i) for i in input().split()]
  lis_aux = [A, B, C]
  return(lis_aux)

def magica(): #Roda oque é pedido para cada teste
  i = 0
  soma = 0
  grafo_dic = {}
  lista_caminhos = [] 
  lista_locais = [] #locais dos pedidos
  grafo_dic[1] = {} #Pizzaria sempre é o nó inicial

  n,m = [int(i) for i in input().split()] #ARMAZENANDO N E M

  i = 1
  while i < n+1: #CRIANDO OS VERTICES NO DICIONARIO
    grafo_dic[i] = {}
    grafo_dic[i][i] = 0 
    i = i+1

  i = 0
  while i != m: #COLOCANDO AS ARESTAS EM UMA LISTA
    r = lendo_ABC()
    grafo_dic[r[0]][r[1]] = r[2] #PREENCHENDO O DICIONÁRIO COM AS ARESTAS
    grafo_dic[r[1]][r[0]] = r[2] #FAZENDO A RECIPROCIDADE
    i = i+1

  quantidade_pizzas = int(input())
  if(quantidade_pizzas == 0):
    return 0
  lista_locais = [int(i) for i in input().split()] #LISTA DE CASAS

  d = Dijkstra(grafo_dic)
  distance = d.dijkstra(1)
  
  for casa in lista_locais: #CONTANDO O PERCURSO
    soma = soma + distance[casa]

  return soma*2 #MULTIPLICANDO POR 2 (IDA E VOLTA)


n_casos = int(input())
i = 0

while i != n_casos:
  resultado = magica()
  #print('caso', i+1,':',resultado)
  print('caso ',end='',flush=True)
  print(i+1,end='',flush=True)
  print(':',end='',flush=True)
  print('',resultado)
  i = i+1