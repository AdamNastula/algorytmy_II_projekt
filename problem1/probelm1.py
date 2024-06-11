import weighted_graph as wg
import  Maksymalne_skojarzenie as ms

def start_problem_1(nazwa_pliku):
    edges = []
    try:
        with open(nazwa_pliku, 'r') as plik:
            for linia in plik:
                # Usunięcie białych znaków z początku i końca linii
                linia = linia.strip()
                # Podzielenie linii na dwa stringi oddzielone spacją
                strings = linia.split(maxsplit=1)
                # Sprawdzenie, czy linia zawiera dokładnie dwa stringi
                if len(strings) == 2:
                    edges.append(wg.Edge(strings[0], strings[1], 1, 0))
                else:
                    print(f"Pominięto niepoprawną linię: {linia}")
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    graph = wg.Graph(edges)
    skoja = ms.Max_Skoj(graph)
    skoja.print_connections()


if __name__ == "__main__":
    plik="problem1_wejscie.txt"
    start_problem_1(plik)