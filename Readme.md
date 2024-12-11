# Algoritmos de Grafos

Este repositorio contiene una colección de algoritmos de grafos implementados en Python. Los algoritmos incluyen métodos para trabajar con grafos dirigidos y no dirigidos, ponderados y no ponderados, y cada implementación está acompañada de ejemplos y análisis de complejidad.
- Se hace en python y sin crear clases, atributos o constructores para facilitar su entendimiento y lectura.
- Dentro de cada carpeta se encuentran los algoritmos correspondientes y la solución a problemas tipicos para estos algoritmos.

## Contenido

- [Descripción de los Algoritmos](#descripción-de-los-algoritmos)
- [Grafos de Ejemplo](#grafos-de-ejemplo)
- [Complejidades de los Algoritmos](#complejidades-de-los-algoritmos)

## Descripción de los Algoritmos

Este repositorio incluye los siguientes algoritmos de grafos:

1. **Búsqueda en Profundidad (DFS)**  
   Implementación de la búsqueda en profundidad en grafos dirigidos y no dirigidos.

2. **Búsqueda en Amplitud (BFS)**  
   Implementación de la búsqueda en amplitud.

3. **DFO**  
   Algoritmo para encontrar el camino más corto desde un nodo fuente a todos los demás nodos en un grafo ponderado.

3. **Kosajaru**  
   Algoritmo para encontrar el camino más corto desde un nodo fuente a todos los demás nodos en un grafo ponderado.

4. **Dijkstra**  
   Algoritmo para encontrar el camino más corto desde un nodo fuente a todos los demás nodos en un grafo ponderado.

5. **Prim**  
   Algoritmo para encontrar el árbol de expansión mínimo en un grafo ponderado.

6. **Kruskal**  
   Algoritmo para encontrar el árbol de expansión mínimo en un grafo ponderado.

7. **Floyd-Warshall**  
   Algoritmo para encontrar los caminos más cortos entre todos los pares de nodos.

8. **Bellman-Ford**  
   Algoritmo para encontrar el camino más corto desde un nodo fuente en un grafo que puede tener aristas con pesos negativos.
9. **Ford-Fulkerson**  
   Algoritmo para calcular el flujo máximo en un grafo de flujo.
10. **Dinic**  
   Algoritmo para calcular el flujo máximo en un grafo de flujo.

## Grafos de Ejemplo

A continuación se muestran algunos ejemplos de grafos utilizados en las implementaciones:

1. **Grafo 1**: <br>
   ![image](https://github.com/user-attachments/assets/9eb93a1c-ce80-43a4-9a46-ac53fc5ef49e)

2. **Grafo 2**: <br>
   ![image](https://github.com/user-attachments/assets/cf3fcfb3-0954-4982-a498-91136129fedd)

3. **Grafo 3**:<br>
   ![image](https://github.com/user-attachments/assets/a1ec75d4-5bcd-47e3-b699-0a182c0a2867)


4. **Grafo 4**:<br>
   ![image](https://github.com/user-attachments/assets/f9c69c51-7bb8-4205-93e5-ee8531ce20ab)


5. **Grafo 5**:<br>
   ![image](https://github.com/user-attachments/assets/9eb93a1c-ce80-43a4-9a46-ac53fc5ef49e)

6. **Grafo 6**:<br>
   ![image](https://github.com/user-attachments/assets/9eb93a1c-ce80-43a4-9a46-ac53fc5ef49e)


## Complejidades de los Algoritmos

| Algoritmo         | Complejidad Temporal          | Complejidad Espacial   |
|--------------------|-------------------------------|-------------------------|
| Búsqueda en Profundidad (DFS) | O(V + E)                       | O(V)                    |
| Búsqueda en Amplitud (BFS)    | O(V + E)                       | O(V)                    |
| Dijkstra                     | O((V + E) log V)               | O(V)                    |
| Prim                         | O(E log V)                     | O(V)                    |
| Kruskal                      | O(E log E)                     | O(V)                    |
| Floyd-Warshall               | O(V³)                          | O(V²)                   |
| Bellman-Ford                 | O(V * E)                       | O(V)                    |
| Ford-Fulkerson               | O(E * f)                       | O(V)                    |

- **V**: Número de vértices
- **E**: Número de aristas
- **f**: Valor máximo del flujo
