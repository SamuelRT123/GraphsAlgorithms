import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr


def dfs(grafo):
    #Tomamos el primer nodo del grafo como origen
    origen= list(grafo.keys())[0]
    
    pila = [origen]
    visitados = set()
    
    while pila:
        nodo = pila.pop() 
        if nodo not in visitados:
            print(nodo) 
            visitados.add(nodo)
                
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    pila.append(vecino)

grafo1= gr.Grafo1()
grafo2= gr.Grafo2()

dfs(grafo1)