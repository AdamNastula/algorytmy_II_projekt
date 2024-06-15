import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

from problem1.weighted_graph import Edge, Graph
from problem1.maximum_association import Max_association

def parse_edges_to_df(edges: Edge = []) -> dict:
    data = {
        'source': [],
        'target': [],
        'weight': [],
    }

    for edge in edges:
        data['source'].append(edge.first)
        data['target'].append(edge.second)
        data['weight'].append(edge.capacity)

        data['source'].append(edge.second)
        data['target'].append(edge.first)
        data['weight'].append(edge.flow)

    return data


def parse_edges_to_ma_df(edges: Edge = []) -> dict:
    data = {
        'source': [],
        'target': [],
    }

    for edge in edges:
        data['source'].append(edge.second)
        data['target'].append(edge.first)

    return data


# wierzcholki sa ustawione w taki sposob, zeby byly po 3 w rzedzie, mozna to zmienic,
# edytujac wartosc z mod. inaczej by sie generowaly losowo i grafy czesto byly nieczytelne
def generate_nodes_positions(edges: Edge = []):
    nodes = set()

    for edge in edges:
        nodes.add(edge.first)
        nodes.add(edge.second)

    sorted_nodes = sorted(nodes)
    nodes_dict = {}
    y = 0
    nodes_number_in_row = 6

    for x in range(len(sorted_nodes)):
        if x % nodes_number_in_row == 0:
            y += 1
            
        nodes_dict[sorted_nodes[x]] = (x % nodes_number_in_row, y)

    return nodes_dict


def generate_ma_nodes_positions(edges, rows):
    nodes = set()

    for edge in edges:
        nodes.add(edge.first)
        nodes.add(edge.second)

    sorted_nodes = sorted(nodes)
    nodes_dict = {}

    y1 = 0
    y2 = 0

    for x in range(len(sorted_nodes)):
        if sorted_nodes[x] in rows[0]:
                nodes_dict[sorted_nodes[x]] = (1, y1)
                y1 += 1
                continue
        elif sorted_nodes[x] in rows[1]:
                nodes_dict[sorted_nodes[x]] = (2, y2)
                y2 += 1
                continue
        elif sorted_nodes[x] == "Start":
            nodes_dict[sorted_nodes[x]] = (0, len(rows[0]) // 2)
        elif sorted_nodes[x] == "End":
            nodes_dict[sorted_nodes[x]] = (3, len(rows[1]) // 2)


    return nodes_dict


def get_edges(argument):
    edges = []
    if type (argument) is Graph:
        edges = argument.parse_graph_to_edges()
    elif type (argument) is list:
        edges = argument
    elif type (argument) is Max_association:
        rows = [argument.front_hands, argument.back_hands]
        edges = argument.graph.edges
        return (edges, rows)

    return edges


def draw_graph(argument):
    edges = get_edges(argument)
    data = parse_edges_to_df(edges)
    df = pd.DataFrame(data)
    graph = nx.MultiDiGraph()

    # dodawanie krawedzi z dataframe
    for _, row in df.iterrows():
        graph.add_edge(row['source'], row['target'], weight=row['weight'])

    # trzeba zwiekszyc wielkosc okienka i drawarea, aby miec pewnosc, ze caly graf sie zmiesci
    position = generate_nodes_positions(edges)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    # dodawanie wiercholkow i wag
    nx.draw_networkx_nodes(graph, position, ax=ax)
    nx.draw_networkx_labels(graph, position, ax=ax, font_size=8)

    # rysowanie
    for (u, v, key, d) in graph.edges(data=True, keys=True):
        nx.draw_networkx_edges(
            graph, position, edgelist=[(u, v)], ax=ax, edge_color=['blue'], width=2,
            arrows=True, arrowstyle='-|>', connectionstyle=f'arc3,rad={0.1 * (key + 1)}'
        )

        x = (position[u][0] + position[v][0]) / 2
        y = (position[u][1] + position[v][1]) / 2

        offset_x = (position[v][1] - position[u][1]) * 0.1 * (key + 1)
        offset_y = (position[u][0] - position[v][0]) * 0.1 * (key + 1)
        ax.text(x + offset_x, y + offset_y, f'{d["weight"]}', fontsize=8, ha='center', va='center')

    plt.show()

def get_chosen_connections(graph: Max_association):
    max_connections = []

    for node in sorted(graph.edmonds.graph.node_list):
        if (node in graph.back_hands and graph.edmonds.graph.adjacency_list[node][0]!="End"):
            max_connections.append((graph.edmonds.graph.adjacency_list[node][0], node))

    return max_connections

def draw_maximum_association(argument):
    edges, rows = get_edges(argument)
    data = parse_edges_to_ma_df(edges)
    df = pd.DataFrame(data)
    graph = nx.MultiDiGraph()

    max_connections = get_chosen_connections(argument)

    # dodawanie krawedzi z dataframe
    for _, row in df.iterrows():
        graph.add_edge(row['source'], row['target'])

    # trzeba zwiekszyc wielkosc okienka i drawarea, aby miec pewnosc, ze caly graf sie zmiesci
    position = generate_ma_nodes_positions(edges, rows)
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95)

    # dodawanie wiercholkow i wag
    nx.draw_networkx_nodes(graph, position, ax=ax, node_size=900, node_color="#CAA5FF")
    nx.draw_networkx_labels(graph, position, ax=ax, font_size=8)

    # rysowanie
    for (u, v, key, d) in graph.edges(data=True, keys=True):
        if (u, v) in max_connections:
            nx.draw_networkx_edges(
                graph, position, edgelist=[(u, v)], ax=ax, edge_color=['#5E81FF'], width=2,
                arrows=True, arrowstyle='-', connectionstyle=f'arc3,rad={0.1 * (key + 1)}'
            )
        else:
            nx.draw_networkx_edges(
                graph, position, edgelist=[(u, v)], ax=ax, edge_color=['#CCEAFF'], width=2,
                arrows=True, arrowstyle='-', connectionstyle=f'arc3,rad={0.1 * (key + 1)}'
            )

    plt.show()  


if __name__ == "__main__":
    edges = [
        Edge("Ludie", "Richard", 1, 0),
        Edge("Ludie", "Joseph", 1, 0),
        Edge("Laura", "Frank", 1, 0),
        Edge("Lesliet", "Albert", 1, 0),
        Edge("Kevin", "Joseph", 1, 0),
        Edge("Donna", "Mary", 1, 0),
        Edge("Ludie", "Albert", 1, 0),
        Edge("Jille", "Mary", 1, 0)
    ]

    graph = Graph(edges)
    max = Max_association(graph)
    
    draw_maximum_association(max)

    # draw_graph(edges)