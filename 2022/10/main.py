import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    register = 1
    cycle = 0
    history = {0: 1}
    for line in infile:
        line = line.strip().split()
        if line[0] == 'noop':
            cycle +=1
            history[cycle] = register
        elif line[0] == 'addx':
            register += int(line[1])
            cycle += 2
            if cycle > 1:
                history[cycle - 1] = history[cycle - 2]
            history[cycle] = register
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    part1_sum = 0
    for cycle in interesting_cycles:
        part1_sum += cycle * history[cycle - 1]


    print(f"Part1: {part1_sum}")
    print(history)
    print_crt(history)

def print_crt(history: dict) -> None:
    # TODO column 1 is buggy
    for i in range(len(history)):
        if history[i] in [(i-1)%40, i%40, (i+1)%40]:
            print("#", end='')
        else:
            print(".", end='')
        if i % 40 == 39:
            print()




print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("Real")
with open(infile, 'r') as infile:
    solution(infile)
