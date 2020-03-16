import networkx as nx
import matplotlib.pyplot as plt
import os.path
from os import path
import sys

def _ReadFromFile_():
    if (path.exists("Arestas.txt")):
        f = open("Arestas.txt", "r")
        l = f.readlines()
        f.close()
        return l
    else:
        print("Não existe o arquivo 'Arestas.txt' no diretorio.")
        sys.exit(0)

def _AddEdgeInGraph_(a):
    for e in a:
        e = e[:-1]
        edge = e.split(",")
        print(edge)
        G.add_edge(edge[0], edge[1])
        
G = nx.Graph()
Arestas = _ReadFromFile_()
_AddEdgeInGraph_(Arestas)
baseColorMap = ["green", "blue", "red", "orange", "yellow"]
i = 0
colorMap = []
for nd in G.nodes:
    for vizinho in G[nd]:
        print(vizinho)
    G._node[nd]["color"] = "green"
    i+= 1
    colorMap.append(G._node[nd]["color"])
nx.draw(G, node_color = colorMap,with_labels=True)
plt.show()
