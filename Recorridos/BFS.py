import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr
import heapq
from collections import deque

def bfs(grafo):
    # Primer nodo del grafo como origen
    origen = list(grafo.keys())[0]
    cola = deque([origen])
    visitados = set()

    while cola:
        nodo = cola.popleft()  # Sacar el primer elemento de la cola, diferente de usar solo pop()
        if nodo not in visitados:
            print(nodo)
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)


#Ejemplo de uso

def es_bipartito(grafo):
    """
    Verifica si un grafo es bipartito.
    """
    n = len(grafo)
    # Todos los vértices inicialmente no coloreados
    color = [-1] * n
    
    for inicio in range(n):
        if color[inicio] == -1:
            cola = deque([inicio])
            color[inicio] = 0
            
            while cola:
                actual = cola.popleft()
                
                for vecino in grafo[actual]:
                    if color[vecino] == -1:
                        #No puede haber 2 colores iguales conectados, conecta con el opuesto
                        color[vecino] = 1 - color[actual]
                        cola.append(vecino)
                    elif color[vecino] == color[actual]:
                        return False
    return True


grafo1 = gr.Grafo1()
grafo2 = gr.Grafo2()

bfs(grafo1)
