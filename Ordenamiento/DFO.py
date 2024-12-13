def DFO(graph):
    visited = set()  
    order = []       


    for node in graph:
        if node not in visited:
            dfs(node,graph,visited,order)

    return order[::-1]


def dfs(node, graph,visited,order):
    if node not in visited:
        visited.add(node)  
        for neighbor in graph[node]:
            dfs(neighbor, graph,visited,order)
        order.append(node)  
        
#Grafo sin ciclos, sino tocara hacer ajustes al algoritmo.
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Orden DFO:", DFO(graph))
