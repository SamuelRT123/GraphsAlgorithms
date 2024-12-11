import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr
import heapq

def find(i, padres):
    if padres[i] != i:
        padres[i] = find(padres[i], padres)
    return padres[i]

def union(nodo1, nodo2, padres, alturas):
    raiz1 = find(nodo1, padres)
    raiz2 = find(nodo2, padres)
    
    if raiz1 != raiz2:
        if alturas[raiz1] > alturas[raiz2]:
            padres[raiz2] = raiz1
        elif alturas[raiz1] < alturas[raiz2]:
            padres[raiz1] = raiz2
        else:
            padres[raiz1] = raiz2
            alturas[raiz2] += 1 
    

def kruskal(grafo,pesos):
    """
    Se puede pasar por parametro una lista de aristas totales que 
    haga bajar la complejidad de la implementación y el algoritmo.
    """
    
    total=0
    arcos=[]
    for vertice in grafo:
        for conexion in grafo[vertice]:
            if vertice!=conexion:
                if vertice+conexion in pesos:
                    peso=pesos[vertice+conexion]
                else:
                    peso=pesos[conexion+vertice]
                
                heapq.heappush(arcos, (peso,vertice,conexion) )
    
    mst=[]
    padres = {v: v for v in grafo}
    alturas = {v: 0 for v in grafo}
    while arcos and len(mst) != len(grafo)-1:
        arco= heapq.heappop(arcos)
        peso, origen, destino= arco
        if find(origen, padres) != find(destino, padres):
            union(origen, destino, padres, alturas)
            mst.append((origen, destino, peso))
            total+=peso
        
    print("El total del camino es: ",total)


grafo3,pesos= gr.Grafo3()
    
kruskal(grafo3,pesos)
