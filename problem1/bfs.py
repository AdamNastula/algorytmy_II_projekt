from collections import deque

import problem1.weighted_graph as wg

"""Od profesora Mroza wyklad 11 (mozna zajrzec jak kod jest niejasny)"""
class bfs:
    def __init__(self, graph):
        self.graph = graph

    def bfs_visit(self, begin_node):
        self.graph.create_adjacency_list()
        colors = dict.fromkeys(self.graph.node_list, 0)
        colors[begin_node] = 1
        queue = deque()
        queue.append(begin_node)
        paths = dict.fromkeys(self.graph.node_list, "")

        while (len(queue) != 0):
            u = queue[0]

            for v in self.graph.adjacency_list[u]:
                if (colors[v] == 0):
                    colors[v] = 1
                    paths[v] = u
                    queue.append(v)
                
            queue.popleft()
            colors[u] = 2

        self.paths = paths

    """Zwraca sciezke "od tylu" (patrz przyklad) w postaci listy kolejno odwiedzanych wierzcholkow"""
    def return_path(self, source, dest):
        path = []

        while (True):
            path.append(dest)

            if (dest == source):
                break
            
            elif (self.paths[dest] == ""):
                path = []
                break

            dest = self.paths[dest]

        return path
        
if __name__ == "__main__":
    edges = []
    edges.append(wg.Edge("A", "B", 1, 2))
    edges.append(wg.Edge("A", "D", 1, 2))
    edges.append(wg.Edge("A", "E", 1, 2))
    edges.append(wg.Edge("D", "E", 1, 2))
    edges.append(wg.Edge("E", "C", 1, 2))
    #edges.append(wg.Edge("C", "D", 1, 2))
    edges.append(wg.Edge("E", "F", 1, 2))
    graph = wg.Graph(edges)
    bfss = bfs(graph)
    bfss.bfs_visit("A")
    print(bfss.return_path("A", "C"))
