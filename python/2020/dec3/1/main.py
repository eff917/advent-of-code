map = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        map.append(line)
treecount = 0
height = len(map)
width = len(map[0])
for j in range(height):
    coordinate = map[j][(3*j)%(width - 1)]
    print(f"{(3*j) % width} {j} {coordinate}")
    if coordinate == '#':
        treecount += 1

print(treecount)