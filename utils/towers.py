import names

import dataclasses
import random
from typing import List

import utils.chans_algorithm as chan
from utils.intersection import Point

@dataclasses.dataclass(frozen=True)
class Tower:
    x: float
    y: float
    brightness: int

@dataclasses.dataclass(frozen=True)
class Flatlander:
    name: str
    energy: int

    def __lt__(self, other):
        return self.energy > other.energy
    
    def __eq__(self, other):
        return self.energy == other.energy

# przyjmuje punkty, tworzy otoczke wypukla i generuje dla kazdego jej punktu jasnosc
def generate_brightness(points: List[Point], range_min, range_max: int) -> List[Tower]:
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
def save_towers_data_to_file(towers: List[Tower]):
    with open('towers_data.txt', 'w') as file:
        file.write(str(len(towers)))
        file.write("\n")

        for tower in towers:
            line = str(tower.x) + " " + str(tower.y) + " " + str(tower.brightness)
            file.write(line)
            file.write("\n")

def generate_flatlanders() -> List[Flatlander]:
    flatlanders = []
    FLATLANDERS_NUM = 20
    MIN_STAMINA = 0
    MAX_STAMINA = 100

    i = 0
    while i < FLATLANDERS_NUM:
        flatlander = Flatlander(names.get_first_name(), random.randint(MIN_STAMINA, MAX_STAMINA))
        if flatlander not in flatlanders:
            flatlanders.append(flatlander)
            i += 1

    return flatlanders

def generate_problem3_data(flatlanders_number, rest_frequency, tower_range_min, tower_range_max, flatlander_range_min, flatlander_range_max):
    random_points_num = 100
    points_min_range = 0
    points_max_range = 200

    random_points = chan.generate_random_points(random_points_num, points_min_range, points_max_range)
    towers = generate_brightness(random_points, tower_range_min, tower_range_max)
    flatlanders = generate_flatlanders(flatlanders_number, flatlander_range_min, flatlander_range_max)

    with open('problem3_data.txt', 'w') as file:
        file.write(str(len(towers)))
        file.write("\n")

        for tower in towers:
            file.write(str(tower.x) + " " + str(tower.y) + " " + str(tower.brightness) + "\n")

        file.write(str(flatlanders_number))
        file.write("\n")

        for flatlander in flatlanders:
            file.write(flatlander.name + " " + str(flatlander.stamina) + "\n")

        file.write(str(rest_frequency))

if __name__ == "__main__":
    # generate_towers(25, 3, 5, 1, 100)
    # towers = generate_brightness([Point(4, 4), Point(4, 6), Point(4, 7),
    #         Point(10, 10), Point(1, 1), Point(1, 1), Point(5, 6), Point(5, 7)], 0, 100)
    # print(towers)

    # tworzenie losowych wiez
    towers2 = generate_brightness(chan.generate_random_points(50, 0, 100), 0, 100)
    # print(towers2)

    print(generate_flatlanders())

    # save_towers_data_to_file(towers2)

    # generate_problem3_data(25, 4, 0, 100, 1, 15)