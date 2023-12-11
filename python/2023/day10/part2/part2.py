import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)


def parse_input(filename: str):
    path = f"{os.path.dirname(os.path.realpath(__file__))}/{filename}"
    map = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            line = f".{line}."
            if map == []:
                top_line = ""
                for i in range(len(line)):
                    top_line += "."
                map.append(top_line)
            map.append(line)
        map.append(top_line)
    return map


def get_starting_position(map) -> tuple[int, int]:
    for y, line in enumerate(map):
        if "S" in line:
            return (y, line.index("S"))


def check_north(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y - 1][node_x] in "|F7":
        return True
    else:
        return False


def check_south(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y + 1][node_x] in "|JL":
        return True
    else:
        return False


def check_east(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y][node_x + 1] in "-J7":
        return True
    else:
        return False


def check_west(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y][node_x - 1] in "-LF":
        return True
    else:
        return False


def get_next_node(current_symbol, current_node, prev_node):
    y_diff = current_node[0] - prev_node[0]
    x_diff = current_node[1] - prev_node[1]
    # prev node is north of current
    if y_diff == 1:
        if current_symbol == "|":
            return (current_node[0] + 1, current_node[1])
        elif current_symbol == "L":
            return (current_node[0], current_node[1] + 1)
        elif current_symbol == "J":
            return (current_node[0], current_node[1] - 1)
        else:
            raise (Exception)

    # prev_node is south of current
    elif y_diff == -1:
        if current_symbol == "|":
            return (current_node[0] - 1, current_node[1])
        elif current_symbol == "F":
            return (current_node[0], current_node[1] + 1)
        elif current_symbol == "7":
            return (current_node[0], current_node[1] - 1)
        else:
            raise (Exception)

    # prev_node is west of current
    elif x_diff == 1:
        if current_symbol == "-":
            return (current_node[0], current_node[1] + 1)
        elif current_symbol == "J":
            return (current_node[0] - 1, current_node[1])
        elif current_symbol == "7":
            return (current_node[0] + 1, current_node[1])
        else:
            raise (Exception)
    # prev_node is east of current
    elif x_diff == -1:
        if current_symbol == "-":
            return (current_node[0], current_node[1] - 1)
        elif current_symbol == "L":
            return (current_node[0] - 1, current_node[1])
        elif current_symbol == "F":
            return (current_node[0] + 1, current_node[1])
        else:
            raise (Exception)


def line_get_inside_count(map: list, loop: list[tuple[int, int]], line: int) -> int:
    # go through the line and check how many times the loop crosses
    # even crosses: outside
    # odd crosses inside

    # TODO bugfix odd length horizontal lines
    inside_nodecount = 0
    inside = False
    prev_corner = ""
    for index, symbol in enumerate(map[line]):
        # we are on the loop
        if (line, index) in loop:
            # if we encounter the start symbol, replace it with the appropriate one
            if symbol == "S":
                symbol = get_start_symbol(map=map, start_node=(line, index))
            # we check from left to right
            if symbol == "|":
                # we go from inside to outside and vice versa
                inside = not inside
            # we're still on the loop line
            if symbol == "-":
                pass
            # possible scenarios:
            # F-----J: we switch
            # F-----7: we stay
            # L-----7: we switch
            # L-----J: we stay
            if symbol == "F":
                prev_corner = symbol
            elif symbol == "L":
                prev_corner = symbol
            elif symbol == "J" and prev_corner == "F":
                inside = not inside
            elif symbol == "J" and prev_corner == "7":
                pass
            elif symbol == "7" and prev_corner == "L":
                inside = not inside
            elif symbol == "J" and prev_corner == "L":
                pass
        else:
            # we're not on the loop
            if inside:
                inside_nodecount += 1

    return inside_nodecount

def get_loop(map):
    loop = [get_starting_position(map=map)]
    # get exactly one neighbor of the starting point
    if check_north(map=map, node=loop[0]):
        loop.append((loop[0][0] - 1, loop[0][1]))
    elif check_south(map=map, node=loop[0]):
        loop.append((loop[0][0] + 1, loop[0][1]))
    elif check_east(map=map, node=loop[0]):
        loop.append((loop[0][0], loop[0][1] + 1))
    index = 1
    # print(loop)
    while loop[0] != loop[-1]:
        current_node = loop[index]
        prev_node = loop[index - 1]
        symbol = map[current_node[0]][current_node[1]]
        loop.append(
            get_next_node(
                current_symbol=symbol, current_node=current_node, prev_node=prev_node
            )
        )
        # print(loop)
        index += 1
    return loop


def get_start_symbol(map, start_node) -> str:
    north = check_north(map, start_node)
    south = check_south(map, start_node)
    east = check_east(map, start_node)
    west = check_west(map, start_node)

    if north and south:
        return "|"
    elif north and east:
        return "L"
    elif north and west:
        return "J"
    elif east and west:
        return "-"
    elif south and east:
        return "F"
    elif south and west:
        return "7"

def main(infile):
    answer = 0
    map = parse_input(infile)
    print(map)
    # add starting point to loop list
    loop = get_loop(map=map)
    print(loop)

    incount = 0
    for index in range(len(map)):
        incount += line_get_inside_count(map=map, loop=loop, line=index)
    answer = incount
    return answer


if __name__ == "__main__":
    infile = "input.txt"
    answer = main(infile)
    print(answer)
