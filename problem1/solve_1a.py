import problem1.weighted_graph as wg
import  problem1.maximum_association as ms

def solve_problem_1a(friends_list):
    print(f"Do zbudowania plotu zostaje wyznaczone {len(friends_list)} plaszczakow")
    for pair in friends_list:
        print(pair[0] + " " + pair[1])

    print("Tworzymy maksymalne skojarzenie otrzymanych par.")

    edges = []
    for friends in friends_list:
        if len(friends) == 2:
            edges.append(wg.Edge(friends[0], friends[1], 1, 0))
        else:
            print("Nieprawidłowa liczba elementów w linii")
    graph = wg.Graph(edges)
    family = ms.Max_association(graph)
    family.print_connections()

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

