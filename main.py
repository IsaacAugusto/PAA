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
        G.add_edge(edge[0], edge[1])

def _SetAllNodeColorsToGray_(g):
    for nod in g.nodes:
        g._node[nod]['color'] = "gray"

G = nx.Graph()
Arestas = _ReadFromFile_()
_AddEdgeInGraph_(Arestas)
_SetAllNodeColorsToGray_(G)
baseColorMap = ["blue", "green", "red", "orange", "yellow", "pink", "brown", "black", "white"]
i = 0
colorMap = []
for nd in G.nodes:
    colorChoices = baseColorMap[:]
    i = 0
    for vizinho in G[nd]:
        if (G._node[vizinho]["color"] in colorChoices):
            colorChoices.remove(G._node[vizinho]["color"])
    if len(colorChoices) > 0:
        G._node[nd]["color"] = colorChoices[0]
    else:
        G._node[nd]["color"] = "gray"
    colorMap.append(G._node[nd]["color"])
nx.draw(G, node_color = colorMap,with_labels=True)
plt.show()
