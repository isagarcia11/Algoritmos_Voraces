# Algoritmo de Kruskal y Prim para el Árbol de Recubrimiento Mínimo (MST)

# Estructura Union-Find para detectar ciclos (usada en Kruskal)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Cada nodo es su propio padre inicialmente
        self.rank = [0] * n           # Rango para optimización

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compresión de caminos
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Unión por rango
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

# Algoritmo de Kruskal
def kruskal(n, edges):
    # edges: lista de tuplas (u, v, costo) representando las aristas
    # n: número de nodos (municipios)

    # Ordenar aristas por costo
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)  # Inicializar Union-Find
    mst = []           # Lista para almacenar las aristas del MST
    total_cost = 0     # Costo total del MST
    edges_added = 0    # Contador de aristas agregadas

    for u, v, cost in edges:
        if uf.union(u, v):  # Si no forma ciclo
            mst.append((u, v, cost))
            total_cost += cost
            edges_added += 1
            if edges_added == n - 1:  # MST completo
                break
    
    return mst, total_cost

# Algoritmo de Prim
from heapq import heappush, heappop

def prim(n, adj_list):
    # adj_list: lista de adyacencia donde adj_list[u] = [(v, costo), ...]
    # n: número de nodos (municipios)

    visited = [False] * n
    min_heap = []
    mst = []
    total_cost = 0
    edges_added = 0

    # Comenzar desde el nodo 0
    visited[0] = True
    for v, cost in adj_list[0]:
        heappush(min_heap, (cost, 0, v))

    while min_heap and edges_added < n - 1:
        cost, u, v = heappop(min_heap)
        if visited[v]:
            continue
        
        mst.append((u, v, cost))
        total_cost += cost
        edges_added += 1
        visited[v] = True

        for next_v, next_cost in adj_list[v]:
            if not visited[next_v]:
                heappush(min_heap, (next_cost, v, next_v))

    return mst, total_cost
