import dataclasses
from typing import Set, Union, List

@dataclasses.dataclass()
class Edge():
    first: Union[int, str]
    second: Union[int, str]
    u: int
    v: int

    def __str__(self):
        return f'pierwszy wierzcholek: {self.first}, drugi wierzcholek: {self.second}, u: {self.u}, v: {self.v}'


class Graph:
    def __init__(self, edges: List[Edge] = []):
        self.edges = edges
        self.node_list: Set[str] = set()
        self.__unpack_nodes()

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

    """Wewnętrzna funkcja. Zapsiuje na set wszystkie wierzcholki w grafie."""
    def __unpack_nodes(self):
        for edge in self.edges:
            self.node_list.add(edge.first)
            self.node_list.add(edge.second)


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