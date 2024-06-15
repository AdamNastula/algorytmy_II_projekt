import problem1.weighted_graph as wg
import  problem1.maximum_association as ms
from utils.draw_graph import draw_maximum_association

def solve_problem_1a(friends_list):
    edges = []
    for friends in friends_list:
        if len(friends) == 2:
            edges.append(wg.Edge(friends[0], friends[1], 1, 0))
        else:
            print("Nieprawidłowa liczba elementów w linii")
    graph = wg.Graph(edges)
    family = ms.Max_association(graph)
    family.print_connections()
    draw_maximum_association(family)

def test():
    data= [
        ["Artur","Franciszek"],
        ["Beata","Franciszek"],
        ["Beata","Henryk"],
        ["Celina","Gerard"],
        ["Celina","Henryk"],
        ["Celina","Ignacy"],
        ["Daniel","Henryk"],
        ["Edward","Henryk"]
    ]
    solve_problem_1a(data)

if __name__ == "__main__":
    test()

