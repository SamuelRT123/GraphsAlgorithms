import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr
import heapq
from collections import deque

def bfs(grafo):
    #Usualmente el origen se pasa por parametro
    origen= list(grafo.keys())[0]
    cola= deque()
    visitados={origen:True}
    cola.append(origen)
    print(origen)
    while cola:
        origen = cola.pop()
        for conexion in grafo[origen]:
            if conexion not in visitados:
                cola.append(conexion)
                visitados[conexion] = True
                print(conexion)
            
    #Para saber si el grafo es conexo
    """
        if len(visitados) == len(grafo):
            return True
        else:
            return False
    """
            
def encontrarCamino(grafo, origen, destino):
    """
    BFS encuentra el camino más "rapido" en terminos de números de aristas.
    """
    visitados={}
    cola= deque()
    cola.append(origen)
    camino={}
    camino[destino]=None
    terminar=False
    while cola and not terminar:
        inicio= cola.popleft()
        for conexion in grafo[inicio]:
            if conexion not in visitados:
                visitados[conexion] = True
                cola.append(conexion)
                camino[conexion]= inicio
                if conexion == destino:
                    terminar=True
                    break
    return camino
    
def detectarCiclosDirigidos(grafo):
    
    visitados={}
    origen= list(grafo.keys())[5]
    
    cola= deque()
    cola.append(origen)
    ciclo={}
    while cola:
        padre = cola.popleft()
        for hijo in grafo[padre]:
            if hijo in visitados:
                print(ciclo)
                return True
            else:
                visitados[hijo] = True
                ciclo[hijo]=padre
                cola.append(hijo)
    return False

def detectarBipartito(grafo):
    pass

def detectarConjuntos(grafo):
    """
    El algoritmo generalizado para saber si un grafo es bipartito o
    algo que se invente como tripartito.
    """
    pass
grafo1= gr.Grafo1()
grafo2= gr.Grafo2()
#grafo3= gr.Grafo3()
#grafo4= gr.Grafo4()

#bfs normal
#bfs(grafo1)
#Adaptaciones del bfs ---------------------------------------------
print("Camino entre 2 puntos" + "-"*25)
origen="0"
destino="10"
camino=encontrarCamino(grafo1,origen,destino)
print(destino)
while origen != destino:
    inicio= camino[destino]
    destino=inicio
    print(destino)
    
    
print("Detectar ciclos en un grafo" + "-"*25)
if detectarCiclos(grafo2):
    print("El grafo tiene ciclos.")
else:
    print("No hay ciclos.")