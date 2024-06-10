from greedy_alg import *
import heapq

class plaszczak:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    
    def __lt__(self, other):
        return self.energy > other.energy
    
    def __eq__(self, other):
        return self.energy == other.energy

towers = []
plaszczaki = []
towers_quantity = int(input())

for i in range(towers_quantity):
    line = input()
    splitted_line = line.split()
    towers.append(tower(splitted_line[0], splitted_line[1], int(splitted_line[2])))

plaszczaki_quantity = int(input())

for i in range(plaszczaki_quantity):
    line = input()
    splitted_line = line.split()
    plaszczaki.append(plaszczak(splitted_line[0], int(splitted_line[1])))

towers.append(towers[0])
max_distance = int(input())
rest_spots = []
rests_quantity = find_rest_spots(0, None, max_distance, 0, towers, rest_spots)
print(rests_quantity)
print(rest_spots)
heapq.heapify(plaszczaki)

for i in range(7):
    max_plaszczak = heapq.heappop(plaszczaki)
    print(max_plaszczak.name, " ", max_plaszczak.energy)