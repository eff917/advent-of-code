instructions = []
with open('2020/dec12/input.txt', 'r') as inputfile:
    for line in inputfile:
        direction  = line[0]
        distance = int(line[1:])
        instructions.append([direction, distance])

EW = 0
NS = 0
# North: 0
# East: 1
# South: 2
# West: 3
orientation = 1
for instruction in instructions:
    print(instruction)
    # cardinal directions
    if instruction[0] == 'N':
        NS += instruction[1]
    elif instruction[0] == 'S':
        NS -= instruction[1]
    elif instruction[0] == 'E':
        EW += instruction[1]
    elif instruction[0] == 'W':
        EW -= instruction[1]
    # forward base on orientation
    elif instruction[0] == 'F':
        if orientation == 0:
            NS += instruction[1]
        elif orientation == 1:
            EW += instruction[1]
        elif orientation == 2:
            NS -= instruction[1]
        elif orientation == 3:
            EW -= instruction[1]
    # turn right
    elif instruction[0] == 'R':
            orientation += instruction[1]//90
            orientation = orientation%4
    # turn left
    elif instruction[0] == 'L':
            orientation -= instruction[1]//90
            orientation = orientation%4
    print(NS, EW)

print(abs(EW) + abs(NS))

