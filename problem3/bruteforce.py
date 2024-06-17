from utils.towers import Tower    

def find_paths(start, old, max_path, rests, towers_list, return_list):
    if (old != None):
        if (towers_list[old].brightness < towers_list[start].brightness):
            rests += 1

    if (start == len(towers_list) - 1):
        return_list.append(rests)
        return
    
    for j in range(max_path):
        if (start + j + 1 >= len(towers_list)):
            break
        
        find_paths(start + j + 1, start, max_path, rests, towers_list, return_list)

def test_bruteforce(start, old, max_path, rests, towers_list, return_list):
    find_paths(start, old, max_path, rests, towers_list, return_list)
    return min(return_list)

if __name__ == "__main__":
    towers = []
    plaszczaki = []
    towers_quantity = int(input())

    for i in range(towers_quantity):
        line = input()
        splitline = line.split()
        towers.append(Tower(splitline[0], splitline[1], splitline[2]))

    plaszczaki_quantity = int(input())

    for i in range(plaszczaki_quantity):
        line = input()
        splitline = line.split()
        plaszczaki.append((splitline[0], splitline[1]))

    max_path = int(input())
    return_list = []
    towers.append(towers[0])
    test_bruteforce(0, None, max_path, 0, towers, return_list)
    print(min(return_list))