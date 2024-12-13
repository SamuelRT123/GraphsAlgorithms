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
                    
                    
#Ejemplo de uso
def dfs_Tarjan(v, parent, graph, visited, tin, low, bridges, time):
    visited[v] = True
    tin[v] = low[v] = time[0]
    time[0] += 1

    for to in graph[v]:
        if to == parent:
            continue
        if not visited[to]:
            dfs_Tarjan(to, v, graph, visited, tin, low, bridges, time)
            low[v] = min(low[v], low[to])
            # Condición para un puente
            if low[to] > tin[v]:
                bridges.append((v, to))
        else:
            low[v] = min(low[v], tin[to])

def find_bridges(graph):
    n = len(graph)  # Número de nodos (suponiendo grafo indexado desde 0)
    tin = [-1] * n  # Tiempos de descubrimiento
    low = [-1] * n  # Tiempos más bajos alcanzables
    visited = [False] * n  # Nodos visitados
    bridges = []  # Lista para almacenar los puentes
    time = [0]  # Usar una lista para modificar dentro del DFS

    # Ejecutar DFS desde cada componente
    for i in range(n):
        if not visited[i]:
            dfs_Tarjan(i, -1, graph, visited, tin, low, bridges, time)

    return bridges

# Ejemplo de uso
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4],
    4: [3]
}

bridges = find_bridges(graph)
#Si se elimina uno  de esos el grafo ya se conecta.
print("Puentes encontrados:", bridges)


grafo1= gr.Grafo1()
grafo2= gr.Grafo2()

dfs(grafo1)