from copy import deepcopy
from collections import Counter
url = '2021/dec15/input.txt'
# url = '2021/dec15/input-example.txt'

map = []
map_height = 0
map_length = 0
with open(url, 'r') as infile:
    for line in infile:
        map_height +=1
        map.append([int(x) for x in line.strip()])
    map_length = len(line.strip())

# map_height*=5
# map_length*=5

extended_map = []
for line in map:
    eline = []
    for i in range(5):
        for element in line:
            eline.append((element + i)%9 if (element+i)>9 else element+i)
    extended_map.append(eline)

for i in range(1, 5):
    for j in range(map_height):
        line = [(x+i)%9 if (x+i)>9 else x+i for x in extended_map[j]]
        extended_map.append(line)

for line in map:
    print(line)
print()
for line in extended_map:
    print(line)

map_height = len(extended_map)
map_length = len(extended_map[0])

riskmap = []
for line in range(map_height):
    riskmap.append([])
    for width in range(map_length):
        riskmap[line].append(None)

riskmap[0][0] = map[0][0]
# for line in riskmap:
#     print(line)

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
        riskmap[y][x] = min(neighbour_risks) + extended_map[y][x]
    else:
        pass

    mapped.add((y, x))

print(map_length)
for i in range(10):
    for Y in range(map_height):
        for X in range(map_length):
            if Y > 0 or X > 0:
                # print(f"Checking: {Y} {X}")
                calculate_risk(Y, X)
    print(f"Round {i} {riskmap[map_height-1][map_length-1] - riskmap[0][0]}")
    # for line in riskmap:
    #     print(line)

print(riskmap[map_height-1][map_length-1] - riskmap[0][0])