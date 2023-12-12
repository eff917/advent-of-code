import os
import pprint

pp = pprint.PrettyPrinter(indent=2)


def expand_galaxy(galaxy_list, expansion_value):
    for key, y, x in galaxy_list.items():
        pass
    return galaxy_list


def convert_map(
    map: list[str],
) -> tuple[dict[int, tuple[int, int]], list[int], list[int]]:
    galaxy_list = {}
    index = 1
    empty_rows = []
    get_empty_columns = []
    for y, line in enumerate(map):
        if line.count(".") == len(line):
            empty_rows.append(y)
        for x, char in enumerate(line):
            if char == "#":
                galaxy_list[index] = (y, x)
                index += 1
    for x in range(len(map[0])):
        empty = True
        for y in range(len(map)):
            if map[y][x] == "#":
                empty = False
        if empty:
            get_empty_columns.append(x)
    return (galaxy_list, empty_rows, get_empty_columns)


def get_distance(galaxy_list: list, galaxy_1: int, galaxy_2: int) -> int:
    return abs(galaxy_list[galaxy_1][0] - galaxy_list[galaxy_2][0]) + abs(
        galaxy_list[galaxy_1][1] - galaxy_list[galaxy_2][1]
    )


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
    galaxy_list = convert_map(map)
    print("Conversion complete")
    map = expand_galaxy(galaxy_list)
    print("Map expanded")

    # pp.pprint(map)
    # TODO: refactor replace galaxies, to return a list of galaxies with coordinates
    # that way we don't need to loop over the map for every connection
    for key in galaxy_list.keys():
        for i in range(1, key):
            answer += get_distance(galaxy_list, key, i)

    return answer


if __name__ == "__main__":
    infile = "input.txt"
    answer = main(infile)
    print(answer)
