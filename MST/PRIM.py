import sys
import os
import heapq

# Configuración del path para importar el módulo
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr

def PRIM(grafo,pesos):
    origen = list(grafo.keys())[0]
    min_heap = []
    visitado = set()
    mst = []
    total=0
    # Agregar las aristas del nodo inicial
    agregar_aristas(origen, visitado, min_heap, grafo, pesos)

    while min_heap and len(visitado) < len(grafo):
        peso, u, v = heapq.heappop(min_heap)
        if v not in visitado:
            total+=peso
            mst.append((u, v, peso))
            agregar_aristas(v, visitado, min_heap, grafo,pesos)
    
    return total

def agregar_aristas(vertice, visitado, min_heap, grafo, pesos):
    visitado.add(vertice)
    for vecino in grafo[vertice]:
        if vecino not in visitado:
            if vecino!=vertice:
                if vertice+vecino in pesos:
                    heapq.heappush(min_heap, (pesos[vertice+vecino], vertice, vecino))
                else:
                    heapq.heappush(min_heap, (pesos[vecino+vertice], vertice, vecino))

# Crear el grafo
grafo3,pesos = gr.Grafo3()

# Ejecutar el algoritmo de Prim
mst = PRIM(grafo3,pesos)
print("Árbol de expansión mínima:", mst)
