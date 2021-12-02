horizontalp = 0
depth = 0

with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        command, value = line.split(' ')
        print(command, value)
        if command == 'down':
            depth += int(value)
        if command == 'up':
            depth -= int(value)
        if command == 'forward':
            horizontalp += int(value)

print(horizontalp*depth)