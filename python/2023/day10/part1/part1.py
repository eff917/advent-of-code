import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)

def calc_diff(line):
    history = []
    elem1 = line[0]
    for elem2 in line[1:]:
        history.append(elem2-elem1)
        elem1 = elem2

    return history

def extend_top_line(bottom_line, top_line):
    top_line.append(top_line[-1]+bottom_line[-1])
    return top_line


def get_submap_extension_value(submap: list):
    submap.reverse()
    submap[0].append(0)
    for i in range(1, len(submap)):
        submap[i] = extend_top_line(submap[i-1], submap[i])
    return submap[-1][-1]

def parse_input(path: str):
    map = []
    with open(path) as file:
        for line in file:
            line = [int(x) for x in line.split()]
            submap = [line,]
            # print(line)
            while max(line) > 0 or min(line) < 0:
                line = calc_diff(line)
                submap.append(line)
                # print(line)
            map.append(submap)

    return map

def main(infile):
    answer = 0
    map = parse_input(infile)
    # pp.pprint(map)
    for submap in map:
        answer += get_submap_extension_value(submap)
    return answer

if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)