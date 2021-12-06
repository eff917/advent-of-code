instructions = []
with open('2020/dec12/input.txt', 'r') as inputfile:
    for line in inputfile:
        direction  = line[0]
        distance = int(line[1:])
        instructions.append([direction, distance])


waypoint = [10, 1]
location = [0, 0]
# North: 0
# East: 1
# South: 2
# West: 3
for instruction in instructions:
    print(instruction)
    # cardinal directions
    if instruction[0] == 'N':
        waypoint[1] += instruction[1]
    elif instruction[0] == 'S':
        waypoint[1] -= instruction[1]
    elif instruction[0] == 'E':
        waypoint[0] += instruction[1]
    elif instruction[0] == 'W':
        waypoint[0] -= instruction[1]
    # forward 
    elif instruction[0] == 'F':
        location[0] += instruction[1] * waypoint[0]
        location[1] += instruction[1] * waypoint[1]
    # rotate waypoint right
    elif instruction[0] == 'R':
        if instruction[1] == 90:
            waypoint = [waypoint[1], waypoint[0] * -1]
        if instruction[1] == 180:
            waypoint = [waypoint[0] * -1, waypoint[1] * -1]
        if instruction[1] == 270:
            waypoint = [waypoint[1] * -1, waypoint[0]]
        pass
    # rotate waypoint left
    elif instruction[0] == 'L':
        if instruction[1] == 270:
            waypoint = [waypoint[1], waypoint[0] * -1]
        if instruction[1] == 180:
            waypoint = [waypoint[0] * -1, waypoint[1] * -1]
        if instruction[1] == 90:
            waypoint = [waypoint[1] * -1, waypoint[0]]
        pass
    print(waypoint)

print(abs(location[0]) + abs(location[1]))

