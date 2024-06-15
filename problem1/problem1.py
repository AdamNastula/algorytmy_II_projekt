from sys import platform
from pathlib import Path

from utils import intersection
from problem1.solve_1a import solve_problem_1a
from problem1.solve_1b import solve_problem_1b
from utils.towers import generate_flatlanders

flatlanders_quantity = int(input())
flatlanders_pairs = []

for i in range(flatlanders_quantity):
    line = input()
    flatlanders_pairs.append(line.split())

points_quantity = int(input())
points = []

for i in range(points_quantity):
    line = input()
    splitted_line = line.split()
    points.append(intersection.Point(float(splitted_line[0]), float(splitted_line[1])))

solve_problem_1a(flatlanders_pairs)
convex_hull = solve_problem_1b(points)

base_dir = "problem3"
filename = "problem1_result.txt"

path = Path('.') / 'problem3' / 'problem1_result.txt'

with open(path.resolve(), 'w') as file:
    file.write(str(len(convex_hull)) + "\n")
    for point in convex_hull:
        file.write(str(point.x) + " " + str(point.y) + "\n")

    flatlanders = generate_flatlanders()
    file.write(str(len(flatlanders)) + "\n")

    for flatlander in flatlanders:
        file.write(flatlander.name + " " + str(flatlander.energy) + "\n")