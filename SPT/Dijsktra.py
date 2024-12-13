import heapq

def Dijkstra(grafo,origin):
    distTo = {}

    for vertex in grafo:
        if vertex == origin:
            distTo[origin] = 0
        else:
            distTo[vertex] = float('inf')

    minheap = []
    minheapOrigin = (0, origin)
    heapq.heappush(minheap, minheapOrigin)

    while minheap:
        distance, vertex = heapq.heappop(minheap)

        if distance > distTo[vertex]:
            continue

        for conexion in grafo[vertex]:
            nodo, peso = conexion
            if (distance + peso) < distTo[nodo]:
                distTo[nodo] = distance + peso
                heapq.heappush(minheap, (distance + peso, nodo))

    return distTo
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

print("Matriz de distancias más cortas:")
for v in graph:
    row= Dijkstra(graph,v)
    print(list(row.values()))
