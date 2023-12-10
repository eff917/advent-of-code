import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)


def parse_input(path: str):
    map = []
    with open(path) as file:
        for line in file:
            map.append(line.strip())

    return map

def get_starting_position(map):
    for y, line in enumerate(map):
        if 'S' in line:
            return(y, line.index('S'))

def get_connected_neighbours(map: list) -> list:

    return []

def main(infile):
    answer = 0
    map = parse_input(infile)
    print(map)

    return answer

if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)