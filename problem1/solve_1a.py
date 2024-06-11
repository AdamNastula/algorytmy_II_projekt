import weighted_graph as wg
import  maximum_association as ms

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


if __name__ == "__main__":
    data=[["Artur","Franciszek"],
          ["Beata","Franciszek"],
          ["Beata","Henryk"],
          ["Celina","Gerard"],
          ["Celina","Henryk"],
          ["Celina","Ignacy"],
          ["Daniel","Henryk"],
          ["Edward","Henryk"]
          ]
    solve_problem_1a(data)

