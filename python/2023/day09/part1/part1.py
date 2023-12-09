import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)


def parse_input(path: str):
    map = {}
    with open(path) as file:
        for line in file:
            line = line.split()
    return map

def main(infile):
    answer = 0
    map = parse_input(infile)
    return answer

if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)
