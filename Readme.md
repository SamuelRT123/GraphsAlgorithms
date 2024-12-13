# Algoritmos de Grafos

Este repositorio contiene una colección de algoritmos de grafos implementados en Python. Los algoritmos incluyen métodos para trabajar con grafos dirigidos y no dirigidos, ponderados y no ponderados. Cada implementación está acompañada de ejemplos y un análisis de complejidad.

- Se utiliza Python sin crear clases, atributos ni constructores para facilitar la comprensión y lectura.
- Dentro de cada carpeta se encuentran los algoritmos correspondientes y la solución a problemas típicos asociados a estos algoritmos.

## Contenido

- [Descripción de los Algoritmos](#descripción-de-los-algoritmos)
- [Grafos de Ejemplo](#grafos-de-ejemplo)
- [Complejidades de los Algoritmos](#complejidades-de-los-algoritmos)

## Descripción de los Algoritmos

Este repositorio incluye los siguientes algoritmos de grafos:

1. **Búsqueda en Profundidad (DFS)**\
   Realiza un recorrido por los nodos de un grafo explorando tan profundamente como sea posible antes de retroceder. Utilizado en problemas como detección de ciclos y componentes conexos.

2. **Búsqueda en Amplitud (BFS)**\
   Realiza un recorrido nivel por nivel, explorando los nodos vecinos antes de avanzar a la siguiente capa. Comúnmente utilizado para encontrar la distancia mínima en grafos no ponderados.

3. **Ordenación Topológica (DFO)**\
   Encuentra un orden lineal de los vértices en un grafo dirigido acíclico (DAG).&#x20;

4. **Kosaraju**\
   Algoritmo para encontrar componentes fuertemente conexos en grafos dirigidos.

5. **Dijkstra**\
   Encuentra el camino más corto desde un nodo fuente a todos los demás nodos en un grafo con pesos no negativos.

6. **Prim**\
   Encuentra el árbol de expansión mínimo en un grafo ponderado, asegurando que el costo total sea mínimo.

7. **Kruskal**\
   Otro algoritmo para encontrar el árbol de expansión mínimo, trabajando con un enfoque de "aristas primero".

8. **Floyd-Warshall**\
   Calcula los caminos más cortos entre todos los pares de nodos en un grafo, permitiendo pesos negativos.

9. **Bellman-Ford**\
   Encuentra el camino más corto desde un nodo fuente, soportando aristas con pesos negativos y detectando ciclos negativos.

10. **Ford-Fulkerson**\
    Calcula el flujo máximo en un grafo de flujo utilizando un enfoque iterativo basado en aumentos.

11. **Dinic**\
    Optimiza el cálculo del flujo máximo en un grafo de flujo mediante niveles y caminos bloqueados.

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


## Complejidades de los Algoritmos

| Algoritmo                     | Complejidad Temporal | Complejidad Espacial |
| ----------------------------- | -------------------- | -------------------- |
| Búsqueda en Profundidad (DFS) | O(V + E)             | O(V)                 |
| Búsqueda en Amplitud (BFS)    | O(V + E)             | O(V)                 |
| Ordenación Topológica (DFO)   | O(V + E)             | O(V)                 |
| Kosaraju                      | O(V + E)             | O(V)                 |
| Dijkstra                      | O((V + E) log V)     | O(V)                 |
| Prim                          | O(E log V)           | O(V)                 |
| Kruskal                       | O(E log E)           | O(V)                 |
| Floyd-Warshall                | O(V³)                | O(V²)                |
| Bellman-Ford                  | O(V \* E)            | O(V)                 |
| Ford-Fulkerson                | O(E \* f)            | O(V)                 |
| Dinic                         | O(V² \* E)           | O(V + E)             |

- **V**: Número de vértices
- **E**: Número de aristas
- **f**: Valor máximo del flujo

