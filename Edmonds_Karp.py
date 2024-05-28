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
        max_free_capacity=0
        for i in range(index-1):

            first=self.residual.nodes_to_numbers[path[i]]
            second=self.residual.nodes_to_numbers[path[i+1]]
            this_max = self.residual.adjacency_matrix[first][second][0]-self.residual.adjacency_matrix[first][second][1]
            if this_max<max_free_capacity or i==0:
                max_free_capacity=this_max
        return max_free_capacity
    """uaktualnia przepływ w grafie na podanej ścierzce o daną wartość"""
    def update_graph(self,path, value):
        index = len(path)
        for i in range(index - 1):
            temp=value
            first = self.graph.nodes_to_numbers[path[i]]
            second = self.graph.nodes_to_numbers[path[i + 1]]
            self.graph.adjacency_matrix[second][first][1] -= value
            self.graph.adjacency_matrix[first][second][1] += value
    """uaktualnia sięć rezydualną na modyfikowanej ścierzce"""
    def make_residual(self, path):
        index = len(path)
        for i in range(index - 1):
            first = self.graph.nodes_to_numbers[path[i]]
            second = self.graph.nodes_to_numbers[path[i + 1]]
            self.residual.adjacency_matrix[first][second][0] = self.graph.adjacency_matrix[first][second][0] - self.graph.adjacency_matrix[first][second][1]
            self.residual.adjacency_matrix[first][second][1] = 0
            self.residual.adjacency_matrix[second][first][0] = self.graph.adjacency_matrix[second][first][0] - self.graph.adjacency_matrix[second][first][1]
            self.residual.adjacency_matrix[second][first][1] = 0
        self.residual.update_structure()
    """szuka maxymalnego możliwego przepływu z punktu do punktu w grafie"""
    def find_max_flow(self, source, sink):
        max_flow = 0
        while True:
            path = self.find_possible_path(source, sink)
            if path==[]:
                break
            value= self.find_max_path_capacity(path)
            self.update_graph(path, value)
            max_flow += value
            self.make_residual(path)
        self.graph.update_structure()
        return max_flow

if __name__ == "__main__":

    edges = []
    edges.append(wg.Edge("A", "B", 4, 0))
    edges.append(wg.Edge("A", "C", 3, 0))
    edges.append(wg.Edge("C", "E", 2, 0))
    edges.append(wg.Edge("B", "E", 3, 0))
    edges.append(wg.Edge("B", "D", 4, 0))
    edges.append(wg.Edge("D", "E", 1, 0))

    graph = wg.Graph(edges)

    edmonds_karp = EdmondsKarp(graph)
    #graph.print_all_edges()
    max_flow = edmonds_karp.find_max_flow('A', 'E')
    print("Maxymalny przepływ: ",max_flow)
    #graph.print_all_edges()
