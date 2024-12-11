import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..')) 
sys.path.append(parent_dir)

import Grafos as gr
import heapq

def BellmanFord(grafo,origen,pesos,TotalConexiones):
    
    distanceTo={}
    for vertice in grafo:
        if vertice == origen:
            distanceTo[vertice]=0
        else:
            distanceTo[vertice]=float("inf")
    
    for _ in range(len(grafo) - 1):
        for conexion in TotalConexiones:
            origen, verticeDestino= conexion
            if (origen + verticeDestino) in pesos:
                costoArco= pesos[origen+verticeDestino]
            else:
                costoArco=pesos[verticeDestino+origen]
                
            if distanceTo[origen] != float("inf"):
                
                if distanceTo[origen] + costoArco < distanceTo[verticeDestino]:
                    distanceTo[verticeDestino] = distanceTo[origen] + costoArco

    return distanceTo

grafo,pesos,arcos= gr.Grafo4()
print( BellmanFord(grafo,"1",pesos,arcos))