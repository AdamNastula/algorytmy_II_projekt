import weighted_graph as wg
import bfs as bfs_f

import copy

class EdmondsKarp:
    def __init__(self, graph):
        self.graph = graph
        self.graph.create_adjacency_matrix()
        self.graph.update_structure()
        self.residual = copy.deepcopy(graph)
    """Szuka bfs'em możliwego połączenia w sieci rezydualnej i zwraca jej ścierzkę"""
    def find_possible_path(self, source, sink):
        bfss = bfs_f.bfs(self.residual)
        bfss.bfs_visit(source)
        test = bfss.returnPath(source, sink)
        return test
    """Szuka maxymalnego przepływu na podanej ścierzce"""
    def find_max_path_capacity(self, path):
        index = len(path)
        path.reverse()
        max_free_capacity=10000000
        # print("ilosc elementów listy: ", index)
        # print(graph.nodes_to_numbers)
        for i in range(index-1):
            first=self.graph.nodes_to_numbers[path[i]]
            second=self.graph.nodes_to_numbers[path[i+1]]
            this_max = self.graph.adjacency_matrix[first][second][0]-self.graph.adjacency_matrix[first][second][1]
            if this_max<max_free_capacity:
                max_free_capacity=this_max
        #print(max_free_capacity)
        return max_free_capacity
    """uaktualnia przepływ w grafie na podanej ścierzce o daną wartość"""
    def update_graph(self,path, value):
        index = len(path)
        for i in range(index - 1):
            first = self.graph.nodes_to_numbers[path[i]]
            second = self.graph.nodes_to_numbers[path[i + 1]]
            self.graph.adjacency_matrix[first][second][1]+=value
        self.graph.update_structure()
    """tworzy sieć rezydualną na podstawie obecnego grafu"""
    def make_residual(self):
        index=len(self.residual.adjacency_matrix)
        for i in range(index):
            for j in range(index):
                self.residual.adjacency_matrix[i][j]=[0,0]
        for i in range(index):
            for j in range(index):
                self.residual.adjacency_matrix[i][j][0] += self.graph.adjacency_matrix[i][j][0]-self.graph.adjacency_matrix[i][j][1]
                self.residual.adjacency_matrix[j][i][0] += self.graph.adjacency_matrix[i][j][1]
        self.residual.update_structure()
    """szuka maxymalnego możliwego przepływu z punktu do punktu w grafie"""
    def find_max_flow(self, source, sink):
        max_flow = 0
        while True:
            self.make_residual()
            path = self.find_possible_path(source, sink)
            if path==[]:
                break
            value= self.find_max_path_capacity(path)
            self.update_graph(path, value)
            max_flow += value
        return max_flow


if __name__ == "__main__":



    # edges = []
    # edges.append(wg.Edge("A", "B", 4, 0))
    # edges.append(wg.Edge("A", "C", 3, 0))
    # edges.append(wg.Edge("C", "E", 2, 0))
    # edges.append(wg.Edge("B", "E", 3, 0))
    # edges.append(wg.Edge("B", "D", 4, 0))
    # edges.append(wg.Edge("D", "E", 1, 0))
    edges = []
    edges.append(wg.Edge("S", "V1", 16, 0))
    edges.append(wg.Edge("V1", "V3", 12, 0))
    edges.append(wg.Edge("V3", "T", 20, 0))
    edges.append(wg.Edge("S", "V2", 13, 0))
    edges.append(wg.Edge("V2", "V4", 14, 0))
    edges.append(wg.Edge("V4", "T", 4, 0))
    edges.append(wg.Edge("V1", "V2", 10, 0))
    edges.append(wg.Edge("V2", "V1", 4, 0))
    edges.append(wg.Edge("V3", "V2", 9, 0))
    edges.append(wg.Edge("V4", "V3", 7, 0))

    graph = wg.Graph(edges)

    edmonds_karp = EdmondsKarp(graph)
    graph.print_all_edges()
    max_flow = edmonds_karp.find_max_flow('S', 'T')
    print()
    print("dadana wartosc: ",max_flow)
    graph.print_all_edges()
