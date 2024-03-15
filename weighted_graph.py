class Edge():
    def __init__(self, first, second, u, v):
        self.first = first
        self.second = second
        self.u = u
        self.v = v

    def __str__(self):
        return f'pierwszy wierzcholek: {self.first}, drugi wierzcholek: {self.second}, u: {self.u}, v: {self.v}'


class Graph:
    def __init__(self, edges=None):
        self.edges = edges or []
        self.node_list = []
        self.relations_list = {}

    """Dodaje nowa krawedz do grafu"""
    def add_new_connection(self, edge):
        self.edges.append(edge)

    """Wypisuje wszystkie krawedzie w grafie wraz z wagami"""
    def print_all_edges(self):
        for edge in self.edges:
            print(edge)

    """Zapsiuje na liste wszystkie wierzcholki w grafie"""
    def get_all_nodes(self):
        for edge in self.edges:
            if edge.first not in self.node_list:
                self.node_list.append(edge.first)
            if edge.second not in self.node_list:
                self.node_list.append(edge.second)
    
    def print_all_nodes(self):
        print(f'Wszystkie wierzcholki w grafie ({len(self.node_list)}): ', end="")
        for node in self.node_list:
            print(node, end=" ")
        print("")


if __name__ == "__main__":
    edge1 = Edge("A", "B", 1, 2)
    edge2 = Edge("C", "B", 4, 4)
    edge3 = Edge("D", "A", 3, 5)

    edges = [edge1, edge2, edge3]

    graph = Graph(edges)

    graph.print_all_edges()
    graph.get_all_nodes()
    graph.print_all_nodes()

    graph.add_new_connection(Edge("A", "C", 3, 4))
    graph.print_all_edges()
    graph.get_all_nodes()
    graph.print_all_nodes()