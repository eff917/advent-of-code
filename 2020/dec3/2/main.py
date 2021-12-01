map = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        map.append(line)
treecount1 = 0
treecount2 = 0
treecount3 = 0
treecount4 = 0
treecount5 = 0

height = len(map)
width = len(map[0])
for j in range(height):
    coordinate = map[j][(j)%(width - 1)]
    if coordinate == '#':
        treecount1 += 1
    coordinate = map[j][(3*j)%(width - 1)]
    if coordinate == '#':
        treecount2 += 1
    coordinate = map[j][(5*j)%(width - 1)]
    if coordinate == '#':
        treecount3 += 1
    coordinate = map[j][(7*j)%(width - 1)]
    if coordinate == '#':
        treecount4 += 1
    if j%2 == 0:
        coordinate = map[j][(j//2)%(width - 1)]
        if coordinate == '#':
            treecount5 += 1
    

print(treecount1*treecount2*treecount3*treecount4*treecount5)