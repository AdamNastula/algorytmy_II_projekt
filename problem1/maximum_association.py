import problem1.weighted_graph as wg
import problem1.Edmonds_Karp as ek

class Max_association:
    def __init__(self, graph):
        self.graph = graph
        self.graph.create_adjacency_matrix()
        self.graph.update_structure()
        self.front_hands=[]
        self.back_hands=[]
        self.separation_of_nodes()
        self.update_graph()
        self.number_of_pairs=self.calculate_max_connections()
    """Rozdziela płaszczaki na te z rękoma z przodu oraz z tyłu(przyjmując żę zawsze podająć połączenia mówimy żę płaszczak w rękoma przodu lubi płaszczaka, który ma ręce z tyłu)"""
    def separation_of_nodes(self):
        for node in sorted(self.graph.node_list):
            if self.graph.adjacency_list[node]==[]:
                self.back_hands.append(node)
            else:
                self.front_hands.append(node)
    """zmiania graf dwudzielny na graf przygotowany pod algorytm Edmondsa-Karpa"""
    def update_graph(self):
        for node in self.front_hands:
            self.graph.add_new_connection(wg.Edge("Start", node, 1, 0))
        for node in self.back_hands:
            self.graph.add_new_connection(wg.Edge(node, "End", 1, 0))
        self.graph.update_nodes()

    """Szuka maxymalnego przepływu w przygotowanym grafie"""
    def calculate_max_connections(self):
        self.edmonds = ek.EdmondsKarp(self.graph)
        max_flow=self.edmonds.find_max_flow("Start","End")
        return max_flow

    """Wyświetla znalezione połączenia przy maksymalnym przepływie"""
    def print_connections(self):
        print(self.number_of_pairs)
        for node in sorted(self.edmonds.graph.node_list):

            if (node in self.back_hands and self.edmonds.graph.adjacency_list[node][0]!="End"):
                print(self.edmonds.graph.adjacency_list[node][0], node)


if __name__ == "__main__":
    edges = []
    edges.append(wg.Edge("A", "F", 1, 0))
    edges.append(wg.Edge("B", "F", 1, 0))
    edges.append(wg.Edge("B", "H", 1, 0))
    edges.append(wg.Edge("C", "G", 1, 0))
    edges.append(wg.Edge("C", "H", 1, 0))
    edges.append(wg.Edge("C", "I", 1, 0))
    edges.append(wg.Edge("D", "H", 1, 0))
    edges.append(wg.Edge("E", "H", 1, 0))

    graph = wg.Graph(edges)

    # draw_graph(graph)

    Family = Max_association(graph)

    #skoja.edmonds.graph.print_all_connections()
    Family.print_connections()