from copy import deepcopy
from collections import Counter
url = '2021/dec15/input.txt'
url = '2021/dec15/input-example.txt'

map = []
map_height = 0
map_length = 0
with open(url, 'r') as infile:
    for line in infile:
        map_height +=1
        map.append([int(x) for x in line.strip()])
    map_length = len(line.strip())
for line in map:
    print(line)

riskmap = []
for line in range(map_height):
    riskmap.append([])
    for width in range(map_length):
        riskmap[line].append(None)

riskmap[0][0] = map[0][0]
# TODO: calculate the minimal total risk for each neighbor of each point.
for line in riskmap:
    print(line)

mapped = set((0, 0))

def get_neigbour_risks(ay: int, ax: int):
    neighbour_list = []
    if ay > 0 and riskmap[ay-1][ax] is not None:
        neighbour_list.append(riskmap[ay-1][ax])
    if ay < map_height-1:
        neighbour_list.append(riskmap[ay+1][ax])
    if ax > 0:
        neighbour_list.append(riskmap[ay][ax-1])
    if ax < map_length-1:
        neighbour_list.append(riskmap[ay][ax+1])
    return neighbour_list

def calculate_risk(y, x):
    neighbour_risks = [i for i in get_neigbour_risks(y, x) if i]
    if len(neighbour_risks) > 0:
        riskmap[y][x] = min(neighbour_risks) + map[y][x]
    else:
        pass

    mapped.add((y, x))


for i in range(map_length):
    for Y in range(map_height):
        for X in range(map_length):
            if Y > 0 or X > 0:
                # print(f"Checking: {Y} {X}")
                calculate_risk(Y, X)
    print()
    for line in riskmap:
        print(line)

print(riskmap[map_height-1][map_length-1] - riskmap[0][0])