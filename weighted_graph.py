import dataclasses
from typing import Set, Union, List

@dataclasses.dataclass()
class Edge():
    first: Union[int, str]
    second: Union[int, str]
    capacity: int    # przepustowosc         
    flow: int        # przeplyw          

    def __str__(self):
        return f'pierwszy wierzcholek: {self.first}, drugi wierzcholek: {self.second}, przepustowosc: {self.capacity}, przeplyw: {self.flow}'


class Graph:
    def __init__(self, edges: List[Edge] = []):
        self.edges = edges
        self.node_list: Set[str] = set()
        self.adjacency_matrix = []
        self.adjacency_list = {}
        self.nodes_to_numbers = {}
        self.numbers_to_nodes = {}
        self.__unpack_nodes()
        self.__encode_nodes()

    """Wewnętrzna funkcja. Zapsiuje na set wszystkie wierzcholki w grafie."""
    def __unpack_nodes(self):
        for edge in self.edges:
            self.node_list.add(edge.first)
            self.node_list.add(edge.second)

    """Wewnetrzna funkcja. Zamienia node'y z str na liczbe naturalna i przechowuje info w odpowiednich slownikach"""
    def __encode_nodes(self):
        counter = 0

        for node in self.node_list:
            self.nodes_to_numbers[node] = counter
            self.numbers_to_nodes[counter] = node
            counter += 1

    """Dodaje nowa krawedz do grafu"""
    def add_new_connection(self, edge: Edge):
        self.edges.append(edge)
        self.node_list.add(edge.first)
        self.node_list.add(edge.second)

    """Wypisuje wszystkie krawedzie w grafie wraz z wagami"""
    def print_all_edges(self):
        for edge in self.edges:
            print(edge)

    def print_all_nodes(self):
        print(f'Wszystkie wierzcholki w grafie ({len(self.node_list)}): ', end="")
        print(" ".join(sorted(self.node_list)))
    
    """Wypelnia liste sasiedztwa (bez informacji o przeplywie i przepustowosci)"""
    def create_adjacency_list(self):
        for node in self.node_list:
            self.adjacency_list[node] = []
        
        for edge in self.edges:
            self.adjacency_list[edge.first].append(edge.second)
    
    """Wypelnia macierz sasiedztwa (z informacja o przeplywie i przepustowosci)"""
    def create_adjacency_matrix(self):
        self.adjacency_matrix = [[[0, 0] for x in range(len(self.node_list))] for y in range(len(self.node_list))]

        for edge in self.edges:
            self.adjacency_matrix[self.nodes_to_numbers[edge.first]][self.nodes_to_numbers[edge.second]] = [edge.capacity, edge.flow]

    """Funkcja ustawi nowa wartosc przeplywu na podanej sciezce (sciezka taka jaka zwraca bfs)"""
    def update_flow_on_path(self, path, new_flow):
        index = len(path) - 1

        while (index >= 0):
            begin = path[index]
            index -= 1
            end = path[index]
            index -=1

            self.adjacency_matrix[self.nodes_to_numbers[begin]][self.nodes_to_numbers[end]][1] = new_flow



if __name__ == "__main__":
    edge1 = Edge("A", "B", 1, 2)
    edge2 = Edge("C", "B", 4, 4)
    edge3 = Edge("D", "A", 3, 5)

    edges = [edge1, edge2, edge3]

    graph = Graph(edges)

    graph.print_all_edges()
    graph.print_all_nodes()

    graph.add_new_connection(Edge("A", "C", 3, 4))
    graph.print_all_edges()
    graph.print_all_nodes()
    graph.create_adjacency_list()
    graph.create_adjacency_matrix()

    print(graph.nodes_to_numbers)
    print()

    for row in graph.adjacency_matrix:
        print(row)
    
    print()

    for node in graph.node_list:
        print(node, graph.adjacency_list[node])
    
    graph.update_flow_on_path(['B', 'C', 'A'], 10)

    for row in graph.adjacency_matrix:
        print(row)