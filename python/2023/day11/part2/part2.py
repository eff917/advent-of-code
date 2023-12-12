import os
import pprint

pp = pprint.PrettyPrinter(indent=2)


def expand_lines(map: list[str]) -> list[str]:
    new_map = []
    for line in map:
        new_map.append(line)
        if line.count(".") == len(line):
            new_map.append(line)
    return new_map


def expand_columns(map: list[str]) -> list[str]:
    i = 0
    column = ""
    while i < len(map[0]):
        empty = True
        for line in map:
            if line[i] != ".":
                empty = False
        if empty:
            for y in range(len(map)):
                map[y] = map[y][: i + 1] + map[y][i:]
            i += 1
        i += 1
    return map


def expand_map(map: list[str]) -> list[str]:
    map = expand_lines(map=map)
    map = expand_columns(map=map)
    return map


def replace_galaxies(map: list[str]) -> list[str]:
    galaxy_list = {}
    index = 1
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "#":
                galaxy_list[index] = (y, x)
                index += 1
    return galaxy_list


def get_distance(galaxy_list: list, galaxy_1: int, galaxy_2: int) -> int:
    return abs(galaxy_list[galaxy_1][0]-galaxy_list[galaxy_2][0]) + abs(galaxy_list[galaxy_1][1]-galaxy_list[galaxy_2][1])


def parse_input(filename: str):
    path = f"{os.path.dirname(os.path.realpath(__file__))}/{filename}"
    map = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            map.append(line)
    return map


def main(infile):
    answer = 0
    map = parse_input(infile)
    print("Map parsed")
    map = expand_map(map)
    print("Map expanded")
    galaxy_list = replace_galaxies(map)
    print("Galaxies replaced")

    # pp.pprint(map)
    # TODO: refactor replace galaxies, to return a list of galaxies with coordinates
    # that way we don't need to loop over the map for every connection
    for key in galaxy_list.keys():
        for i in range(1,key):
            answer += get_distance(galaxy_list, key, i)

    return answer


if __name__ == "__main__":
    infile = "input.txt"
    answer = main(infile)
    print(answer)
