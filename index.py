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
        if vertex2 not in self.adjacency[vertex1]:
            self.adjacency[vertex1].add(vertex2)

        if vertex1 not in self.adjacency[vertex2]:
            self.adjacency[vertex2].add(vertex1)

    def show_graph(self):
        for vertex, neighbors in self.adjacency.items():
            print(f"{vertex}: {neighbors}")

    def remove_vertex(self, vertex):

        if vertex in self.adjacency:
            vertex_neighbors = self.adjacency[vertex]  # pegando os vizinhos

            for vertex_neighbor in vertex_neighbors:  # indo na lista de adjacencias do vizinho e removendo o vertex
                self.adjacency[vertex_neighbor].discard(vertex)

            del self.adjacency[vertex]

    def remove_edge(self, vertex1, vertex2):

        # vai no vertice, procura o vertice2, remove ele
        if vertex1 in self.adjacency:
            self.adjacency[vertex1].discard(vertex2)

        if vertex2 in self.adjacency:
            self.adjacency[vertex2].discard(vertex1)
        # vai no vertice2, procura o vertice 1, remove ele


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
