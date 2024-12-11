import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr
import heapq

def union():
    pass

def find(vertice):
    pass
    

def kruskal(grafo,pesos):
    """
    Se puede pasar por parametro una lista de aristas totales que 
    haga bajar la complejidad, en el parcial poner la lista en los parametros
    """
    
    total=0
    arcos=[]
    for vertice in grafo:
        for conexion in grafo:
            peso=pesos[vertice+conexion]
            heapq.heappush(arcos, (peso,vertice,conexion) )
    
    mst=[]
    while arcos and len(mst) != len(grafo)-1:
        arco= heapq.heappop(arcos)
        peso, vertice, destino= arco
        if find(vertice) != find(destino):
            union
            mst.append((vertice,destino))
            total+=peso
            
        
    print("El total del camino es: ",total)


grafo3,pesos= gr.grafo3()
    
print(kruskal(grafo3,pesos))
