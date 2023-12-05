import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    map = []
    moves = []
    stacks = {}
    map_parsed = False
    for line in infile:
        line  = line.strip('\n')
        # parse stacks
        if not map_parsed and len(line) > 0:
            map.append(line)
            for i in range(1, (len(line)+1)//4+1):
                if i not in stacks.keys():
                    stacks[i] = []
                stacks[i].append(line[(i-1) * 4 + 1])
        # empty line signaling end of stacks
        elif len(line) == 0:
            map_parsed = True
        # parse moves
        elif map_parsed and len(line) > 0:
            words = line.split(' ')
            moves.append([int(words[1]), int(words[3]), int(words[5])])
    for key, value in stacks.items():
        value = value[0:-1]
        newvalue = []
        for item in value:
            if item != " ":
                newvalue.append(item)
        newvalue.reverse()
        stacks[key] = newvalue
    stacks1 = deepcopy(stacks)
    print(stacks1)
    for count, source, target in moves:
        tempstack = []
        for i in range(count):
            stacks1[target].append(stacks1[source].pop())
            tempstack.append(stacks[source].pop())
        tempstack.reverse()
        stacks[target].extend(tempstack)


    print(stacks)
    # for row in map:
    #     print(row)
    # for row in moves:
    #     print(moves)
    solution1 = ''
    solution2 = ''
    for i in range(len(stacks1.keys())):
        solution1 += stacks1[i+1].pop()
        solution2 += stacks[i+1].pop()

    print(f"Part1: {solution1}")
    print(f"Part2: {solution2}")

    pass
print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("Real")
with open(infile, 'r') as infile:
    solution(infile)
