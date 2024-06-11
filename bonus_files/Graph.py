from collections import defaultdict

class Graph: # klasa bazowa - standardowe rzeczy dla grafu
    def __init__(self, nodes, edges):
        self._graph = defaultdict(set)
        # lista sasiedztwa
        self.node_list = {}
        # macierz sasiedztwa
        self.adjacency_matrix = []
        # macierz incydencji
        self.incident_matrix = []
        # zbior wierzcholkow
        self.nodes = nodes
        # zbior krawedzi
        self.edges = edges
        # jezeli node'y to np 'A', 'B' , 'XY' to zle sie na tym operuje dlatego zamienimy je na 0 1 2 3 i zapamietamy w tych slwonikach
        self.nodes_to_numbers = {}
        self.numbers_to_nodes = {}
        # analogicznie dla krawedzi
        self.edges_to_numbers = {}
        self.numbers_to_edges = {}
        # funkcja wypelnia slowniki powyzej 
        self.encode_nodes_and_edges()

    def encode_nodes_and_edges(self): #funkcja zamienia node'y i krawedzie na liczby naturalne z przedzialu [0, n]
        counter = 0

        for node in self.nodes:
            self.nodes_to_numbers[node] = counter
            self.numbers_to_nodes[counter] = node
            counter += 1

        counter = 0

        for edge in self.edges:
            self.edges_to_numbers[edge] = counter
            self.numbers_to_edges[counter] = edge
            counter += 1

    def print_relations(self):
        for key, value in self.node_list.items():
            print(f'wierzcholek: {key}, polaczenia: {value}')
    
    def print_adjacency_matrix(self):
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
    
    def print_incident_matrix(self):
        for row in self.incident_matrix:
            for number in row:
                if (number != -1):
                    print(" ", end="")

                print(number, end=" ")
            
            print()

class directedGraph(Graph): # klasa reprezentujaca graf skierowany
    def __init__(self, nodes, edges):
        super().__init__(nodes, edges)

    """Wypisuje kazdy wierzcholek i jego powiazania w grafie"""
    def create_node_list(self):
        for node1, node2 in self.edges:
            if node1 in self.node_list:
                self.node_list[node1].append(node2)
            else:
                self.node_list[node1] = [node2]

    def create_adjacency_matrix(self):
        self.adjacency_matrix = [[0 for x in range(len(self.nodes))] for y in range(len(self.nodes))]
        for edge in self.edges:
            node1, node2 = edge

            self.adjacency_matrix[self.nodes_to_numbers[node1]][self.nodes_to_numbers[node2]] = 1
    
    def create_incident_matrix(self):
        self.incident_matrix = [[0 for x in range(len(self.edges))] for y in range(len(self.nodes))]

        for edge in self.edges:
            node1, node2 = edge

            self.incident_matrix[self.nodes_to_numbers[node1]][self.edges_to_numbers[edge]] = 1
            self.incident_matrix[self.nodes_to_numbers[node2]][self.edges_to_numbers[edge]] = -1

class undirectedGraph(Graph): # klasa reprezentujaca graf nieskierowany
    def __init__(self, nodes, edges):
        super().__init__(nodes, edges)

    def create_node_list(self):
        for node1, node2 in self.edges:
            if node1 in self.node_list:
                self.node_list[node1].append(node2)
            else:
                self.node_list[node1] = [node2]
            
            if node2 in self.node_list:
                if node1 not in self.node_list[node2]:
                    self.node_list[node2].append(node1)
            else:
                self.node_list[node2] = [node1]

    def create_adjacency_matrix(self):
        self.adjacency_matrix = [[0 for x in range(len(self.nodes))] for y in range(len(self.nodes))]

        for edge in self.edges:
            node1, node2 = edge

            self.adjacency_matrix[self.nodes_to_numbers[node1]][self.nodes_to_numbers[node2]] = 1
            self.adjacency_matrix[self.nodes_to_numbers[node2]][self.nodes_to_numbers[node1]] = 1
    
    def create_incident_matrix(self):
        self.incident_matrix = [[0 for x in range(len(self.edges))] for y in range(len(self.nodes))]

        for edge in self.edges:
            node1, node2 = edge

            self.incident_matrix[self.nodes_to_numbers[node1]][self.edges_to_numbers[edge]] = 1
            self.incident_matrix[self.nodes_to_numbers[node2]][self.edges_to_numbers[edge]] = 1

if __name__ == "__main__":
    g1 = directedGraph(['X', 'Y'], [('X', 'X'), ('X', 'Y'), ('Y', 'X')])
    g1.create_node_list()
    g1.create_adjacency_matrix()
    g1.print_relations()
    g1.print_adjacency_matrix()
    g1.create_incident_matrix()
    g1.print_incident_matrix()

    g2 = undirectedGraph(['X', 'Y'], [('X', 'X'), ('X', 'Y')])
    g2.create_node_list()
    g2.create_adjacency_matrix()
    g2.create_incident_matrix()
    g2.print_relations()
    g2.print_adjacency_matrix()
    g2.print_incident_matrix()

