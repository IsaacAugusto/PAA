import networkx as nx
import matplotlib.pyplot as plt
import os.path
from os import path
import time
import sys
import random

#Função que lê as arestas criadas pelo gerador de arestas
def _ReadFromFile_():
    if (path.exists("Arestas.txt")):
        f = open("Arestas.txt", "r")
        l = f.readlines()
        f.close()
        return l
    else:
        print("Não existe o arquivo 'Arestas.txt' no diretorio.")
        sys.exit(0)

#Função que adiciona as arestas lidas no grafo
def _AddEdgeInGraph_(a):
    for e in a: #Loop por todas as arestas
        e = e[:-1] #remover \n
        edge = e.split(",") #Separo pela virgula
        G.add_edge(edge[0], edge[1]) #Adiciono a aresta lida

#Pinta todos os nodes para cinza inicialmente, para existir o atributo cor
def _SetAllNodeColorsToGray_(g):
    for nod in g.nodes:
        g._node[nod]['color'] = "gray"

def _AddResults_(node, color):
    return "Torre " +str(node) + " = " + color + "\n"

def _GenerateResultsFile_(rlist):
    print (rlist)
    file = open("Results.txt", "w")
    file.write(rlist)
    file.close()

G = nx.Graph() #Crio o grafo
ResultList = ""
Arestas = _ReadFromFile_() #Leio as arestas
_AddEdgeInGraph_(Arestas) #Adiciono as arestas
_SetAllNodeColorsToGray_(G)#Pinta todas as arestas de cinza
baseColorMap = [] #Cores disponiveis
colorMap = [] #Colormap para fazer a coloração do grafo
start_time = time.time() #Calcular tempo de execução
for nd in G.nodes: #Loop por todos os nodes
    colorChoices = baseColorMap[:] #Clono as cores disponíveis
    for vizinho in G[nd]: #Loop por todos os vizinhos do vertice em questão
        if (G._node[vizinho]["color"] in colorChoices): #Se a cor do vizinho atual ja esta no vetor (já foi colorido)
            colorChoices.remove(G._node[vizinho]["color"]) #Remove aquela cor pois não esta mais disponível
    if len(colorChoices) > 0: #Se não tiver removido todas as cores
        G._node[nd]["color"] = colorChoices[0] #Adiciona a primeira cor disponível restante no vetor
    else:
        myColor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        while (myColor in baseColorMap):
            myColor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        baseColorMap.append(myColor)
        G._node[nd]["color"] = myColor
    colorMap.append(G._node[nd]["color"]) #Adiciona a cor ao mapa de cores
    ResultList += _AddResults_(nd, G._node[nd]["color"])
print("--- %f segundos ---" % (time.time() - start_time))#Calcular tempo de execução

_GenerateResultsFile_(ResultList)
nx.draw(G, node_color = colorMap,with_labels=True) #Desenha o grafo
plt.show() #Mostra em uma janela
