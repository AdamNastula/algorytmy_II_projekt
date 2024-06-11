from collections import defaultdict

class Graph:
    def __init__(self, connections_list, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.node_list = {}  # str -> str[]
        self.add_connections(connections_list)

    """Dodaje relacje miedzy wierzcholkami do dictionary (slownika)"""
    def add_connections(self, connections_list):
        for node1, node2 in connections_list:
            if node1 in self.node_list:
                self.node_list[node1].append(node2)
            elif node1 not in self.node_list:
                self.node_list[node1] = [node2]

    """Wypisuje kazdy wierzcholek i jego powiazania w grafie"""
    def print_relations(self):
        for key, value in self.node_list.items():
            print(f'wierzcholek: {key}, polaczenia: {value}')

    """Wypisuje macierz sasiedzstwa dla podanych wierzcholkow"""
    def print_adjacency_graph(self):
        print(" ", end=" ")
        print(" ".join(list(self.node_list.keys())))
        for key, value in self.node_list.items():
            print(key, end=" ")
            for node in self.node_list.keys():
                if node in self.node_list[key]:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print("")


    def __str__(self):
        return '{}({})'.format(type(self).__name__, self._graph)


if __name__ == '__main__':
    """Wpisz pary wierzcholkow w grafie niewazonym, ktore sa ze soba powiazane w formacie ("pierwszy", "drugi") - tuple"""
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    g = Graph(connections, True)
    g.print_relations()
    g.print_adjacency_graph()