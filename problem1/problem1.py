from utils import intersection
from problem1.solve_1a import solve_problem_1a
from problem1.solve_1b import solve_problem_1b

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
solve_problem_1b(points)