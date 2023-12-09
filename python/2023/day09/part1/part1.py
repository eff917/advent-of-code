import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)


def parse_input(path: str):
    map = {}
    with open(path) as file:
        for line in file:
            line = line.split()
            if len(line)==1:
                instructions = line[0]
            elif len(line) == 4:
                node = line[0]
                left = line[2][1:4]
                right = line[3][0:3]
                map[node] = {"L": left, "R": right}
    return (instructions, map)

def step(position, instruction, map):
    return map[instruction]


def main(infile):
    instructions, map = parse_input(infile)
    position = "AAA"
    i = 0
    instruction = instructions[i]
    instruction_length = len(instructions)
    print(instructions)
    pp.pprint(map)
    answer = 0
    while position != "ZZZ":
        position = step(position=position, instruction=instructions[i%instruction_length], map=map[position])
        i += 1
    return i


if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)
