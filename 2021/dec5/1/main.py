from os import spawnl


maxX = 0
maxY = 0
vents = []
with open('2021/dec5/input.txt', 'r') as inputfile:
    for line in inputfile:
        firstcoord, secondcoord = line.strip().split(' -> ')
        firstX, firstY = firstcoord.split(',')
        secondX, secondY = secondcoord.split(',')
        firstX = int(firstX)
        firstY = int(firstY)
        secondX = int(secondX)
        secondY = int(secondY)
        maxX = max(max(maxX, firstX), secondX)
        maxY = max(max(maxY, firstY), secondY)
        print(firstY, firstX, secondY, secondX)
        vents.append([firstY, firstX, secondY, secondX])

print(maxX, maxY)
ventmap = []
for i in range(maxX + 1):
    ventmap.append([])
    for j in range(maxY + 1):
        ventmap[i].append(0)

def print_map(mymap):
    for row in mymap:
        print(''.join(str(row)))

for vent in vents:
    # horizontal
    if vent[0] == vent[2]:
        for i in range(min(vent[1], vent[3]), max(vent[1], vent[3])+1):
            ventmap[vent[0]][i] += 1
            print(f"adding {vent[0]} {i}")
            pass
    # vertical
    elif vent[1] == vent[3]:
        for i in range(min(vent[0], vent[2]), max(vent[0], vent[2])+1):
            ventmap[i][vent[1]] += 1
            print(f"adding {i} {vent[1]}")
        pass

print_map(ventmap)

hot_field_count = 0
for row in ventmap:
    for col in row:
        if col > 1:
            hot_field_count += 1
print(hot_field_count)
