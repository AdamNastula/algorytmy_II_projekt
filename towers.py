import dataclasses
import random
from typing import List
import chans_algorithm as chan
from intersection import Point

@dataclasses.dataclass(frozen=True)
class Tower:
    x: int
    y: int
    brightness: int

# tymczasowa funkcja, do usuniecia
def generate_towers(number_of_towers, number_of_flatlanders, rest_frequency, range_min, range_max):
    print(number_of_towers)

    for i in range(number_of_towers):
        print(f"{random.randint(range_min, range_max)} {random.randint(range_min, range_max)} {random.randint(1, 100)}")

    print(rest_frequency)

# przyjmuje punkty, tworzy otoczke wypukla i generuje dla kazdego jej punktu jasnosc
def generate_brightness(points: List[Point], range_min: int, range_max: int) -> List[Tower]:
    convex_hull_points = chan.calculate_hull(points)['convex_hull']
    towers = []

    for point in convex_hull_points:
        towers.append(Tower(point.x, point.y, random.randint(range_min, range_max)))

    return towers

# wypisuje dane wiezy jako tekst wraz z ich iloscia na samej gorze
def print_towers_data(towers: List[Tower]):
    print(len(towers))

    for tower in towers:
        print(tower.x, tower.y, tower.brightness)

# zapisuje dane wiezy do pliku .txt
def save__towers_data_to_file(towers: List[Tower]):
    with open('towers_data.py', 'w') as file:
        file.write(str(len(towers)))
        file.write("\n")

        for tower in towers:
            line = str(tower.x) + " " + str(tower.y) + " " + str(tower.brightness)
            file.write(line)
            file.write("\n")

if __name__ == "__main__":
    # generate_towers(25, 3, 5, 1, 100)
    # towers = generate_brightness([Point(4, 4), Point(4, 6), Point(4, 7),
    #         Point(10, 10), Point(1, 1), Point(1, 1), Point(5, 6), Point(5, 7)], 0, 100)
    # print(towers)

    # tworzenie losowych wiezy
    towers2 = generate_brightness(chan.generate_random_points(50, 0, 100), 0, 100)
    # print(towers2)

    save__towers_data_to_file(towers2)