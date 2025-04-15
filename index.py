from collections import deque


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = set()

    def add_edge(self, vertex1, vertex2):

        if vertex1 not in self.adjacency:
            self.add_vertex(vertex1)

        if vertex2 not in self.adjacency:
            self.add_vertex(vertex2)

        # grafo não direcionado: adiciona a aresta nos dois sentidos
        if vertex2 not in self.adjacency.get(vertex1):
            self.adjacency.get(vertex1).add(vertex2)

        if vertex1 not in self.adjacency.get(vertex2):
            self.adjacency.get(vertex2).add(vertex1)

    def show_graph(self):
        for vertex, neighbors in self.adjacency.items():
            print(f"{vertex}: {neighbors}")

    def remove_vertex(self, vertex):

        if vertex in self.adjacency:
            vertex_neighbors = self.adjacency[vertex]  # pegando os vizinhos

            for vertex_neighbor in vertex_neighbors:  # indo na lista de adjacencias do vizinho e removendo o vertex
                self.adjacency.get(vertex_neighbor).discard(vertex)

            del self.adjacency[vertex]

    def remove_edge(self, vertex1, vertex2):

        # vai no vertice, procura o vertice2, remove ele
        if vertex1 in self.adjacency:
            self.adjacency.get(vertex1).discard(vertex2)

        if vertex2 in self.adjacency:
            self.adjacency.get(vertex2).discard(vertex1)
        # vai no vertice2, procura o vertice 1, remove ele

    def degree(self, vertex):
        # Retorna o grau do vertice
        return len(self.adjacency.get(vertex, set()))

    def hasPah(self, start, end):
        return True

    def DFS(self, start, end, visited_vertexs=set()):

        if start == end:
            return True

        # Começa em um vertice, marca ele como visitado
        visited_vertexs.add(start)

        for neighbor in self.adjacency.get(start):
            if neighbor not in visited_vertexs:
                visited_vertexs.add(neighbor)

                if self.DFS(neighbor, end, visited_vertexs):
                    return True

        return False

    def BFS(self, start, end):

        deque_ = deque()
        visited_vertexs = set()

        deque_.append(start)
        visited_vertexs.add(start)

        while len(deque_) > 0:

            current = deque_.popleft()

            if current == end:
                return True

            for neighbor in self.adjacency.get(current, set()):
                if neighbor not in visited_vertexs:
                    visited_vertexs.add(neighbor)
                    deque_.append(neighbor)

        return False


myGraph = Graph()

# Adicionando os vértices
myGraph.add_vertex("A")
myGraph.add_vertex("B")
myGraph.add_vertex("C")
myGraph.add_vertex("D")
myGraph.add_vertex("E")

# Adicionando as arestas
myGraph.add_edge("A", "B")
myGraph.add_edge("B", "C")
myGraph.add_edge("A", "D")
myGraph.add_edge("C", "E")
myGraph.add_edge("B", "E")

myGraph.show_graph()
myGraph.remove_vertex("B")
print('===============================================')
myGraph.show_graph()
print('===============================================')
myGraph.remove_edge("A", "D")
myGraph.show_graph()
