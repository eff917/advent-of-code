horizontalp = 0
depth = 0
aim = 0

with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        command, value = line.split(' ')
        print(command, value)
        if command == 'down':
            aim += int(value)
        if command == 'up':
            aim -= int(value)
        if command == 'forward':
            horizontalp += int(value)
            depth += (aim * int(value))

print(horizontalp*depth)