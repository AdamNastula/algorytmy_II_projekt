"""
2 - ilosc wiez x y jasnosc
1 2 10
2 3 15
3 - ilsoc plasczakow imie stamina
XXXX 10
YYYY 15
XXYY 8
2 - co ile odpoczynek
"""

class tower:
    def __init__(self, x, y, brightness):
        self.x = x
        self.y = y
        self.brightness = brightness 
    

def find_paths(start, old, max_path, rests, towers_list, return_list):
    if (old != None):
        if (towers[old].brightness < towers[start].brightness):
            rests += 1

    if (start == len(towers) - 1):
        return_list.append(rests)
        return
    
    for j in range(max_path):
        if (start + j + 1 >= len(towers_list)):
            break
        
        find_paths(start + j + 1, start, max_path, rests, towers_list, return_list)

towers = []
plaszczaki = []
towers_quantity = int(input())

for i in range(towers_quantity):
    line = input()
    splitline = line.split()
    towers.append(tower(splitline[0], splitline[1], splitline[2]))

plaszczaki_quantity = int(input())

for i in range(plaszczaki_quantity):
    line = input()
    splitline = line.split()
    plaszczaki.append((splitline[0], splitline[1]))

max_path = int(input())
return_list = []
towers.append(towers[0])
find_paths(0, None, max_path, 0, towers, return_list)
print(min(return_list))