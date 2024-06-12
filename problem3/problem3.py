from problem3.greedy_alg import *
from utils.towers import Tower, Flatlander
import heapq

towers = []
flatlanders = []
towers_quantity = int(input())

for i in range(towers_quantity):
    line = input()
    splitted_line = line.split()
    towers.append(Tower(float(splitted_line[0]), float(splitted_line[1]), int(splitted_line[2])))

flatlanders_quantity = int(input())

for i in range(flatlanders_quantity):
    line = input()
    splitted_line = line.split()
    flatlanders.append(Flatlander(splitted_line[0], int(splitted_line[1])))

towers.append(towers[0])
max_distance = int(input())
rest_spots = []
rests_quantity = find_rest_spots(0, None, max_distance, 0, towers, rest_spots)
print(rests_quantity)
print(rest_spots)
heapq.heapify(flatlanders)

for i in range(7):
    max_plaszczak = heapq.heappop(flatlanders)
    print(max_plaszczak.name, " ", max_plaszczak.energy)