import string
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from weighted_graph import Edge

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

# wierzcholki sa ustawione w taki sposob, zeby byly po 3 w rzedzie, mozna to zmienic,
# edytujac wartosc z mod. inaczej by sie generowaly losowo i grafy czesto byly nieczytelne
def generate_nodes_positions(edges: Edge = []):
    nodes = set()
    for edge in edges:
        nodes.add(edge.first)
        nodes.add(edge.second)

    sorted_nodes = sorted(nodes)

    nodes_number = len(edges)
    nodes_dict = {}

    y = 0
    for x in range(nodes_number - 1):
        if x % 3 == 0:
            y += 1
            
        nodes_dict[sorted_nodes[x]] = (x % 3, y)

    return nodes_dict

def draw_graph(edges: Edge = []):
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


if __name__ == "__main__":
    edges = [Edge("A", "B", 4, 0),
            Edge("A", "C", 3, 0),
            Edge("C", "E", 2, 0),
            Edge("B", "E", 3, 0),
            Edge("B", "D", 4, 0),
            Edge("D", "E", 6, 1),
            Edge("G", "A", 1, 0),
            Edge("Z", "A", 5, 7)]

    draw_graph(edges)