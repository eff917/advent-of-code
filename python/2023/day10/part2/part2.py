import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)


def parse_input(path: str):
    map = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            line = f'.{line}.'
            if map == []:
                top_line = ''
                for i in range(len(line)):
                    top_line += '.'
                map.append(top_line)
            map.append(line)
        map.append(top_line)
    return map

def get_starting_position(map) -> tuple[int, int]:
    for y, line in enumerate(map):
        if 'S' in line:
            return(y, line.index('S'))

def check_north(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y-1][node_x] in "|F7":
        return True
    else:
        return False
def check_south(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y+1][node_x] in "|JL":
        return True
    else:
        return False
def check_east(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y][node_x+1] in "-J7":
        return True
    else:
        return False
def check_west(map: list[list], node: tuple[int, int]):
    node_y, node_x = node
    if map[node_y][node_x-1] in "-LF":
        return True
    else:
        return False

def get_next_node(current_symbol, current_node, prev_node):
    y_diff = current_node[0] - prev_node[0]
    x_diff = current_node[1] - prev_node[1]
    # prev node is north of current
    if y_diff == 1:
        if current_symbol == "|":
            return (current_node[0]+1, current_node[1])
        elif current_symbol == "L":
            return (current_node[0], current_node[1]+1)
        elif current_symbol == "J":
            return (current_node[0], current_node[1]-1)
        else:
            raise(Exception)

    # prev_node is south of current
    elif y_diff == -1:
        if current_symbol == "|":
            return (current_node[0]-1, current_node[1])
        elif current_symbol == "F":
            return (current_node[0], current_node[1]+1)
        elif current_symbol == "7":
            return (current_node[0], current_node[1]-1)
        else:
            raise(Exception)

    # prev_node is west of current
    elif x_diff == 1:
        if current_symbol == "-":
            return (current_node[0], current_node[1]+1)
        elif current_symbol == "J":
            return (current_node[0]-1, current_node[1])
        elif current_symbol == "7":
            return (current_node[0]+1, current_node[1])
        else:
            raise(Exception)
    # prev_node is east of current
    elif x_diff == -1:
        if current_symbol == "-":
            return (current_node[0], current_node[1]-1)
        elif current_symbol == "L":
            return (current_node[0]-1, current_node[1])
        elif current_symbol == "F":
            return (current_node[0]+1, current_node[1])
        else:
            raise(Exception)

def main(infile):
    answer = 0
    map = parse_input(infile)
    print(map)
    # add starting point to loop list
    loop = [get_starting_position(map=map)]
    # get exactly one neighbor of the starting point
    if check_north(map=map, node=loop[0]):
        loop.append((loop[0][0]-1, loop[0][1]))
    elif check_south(map=map, node=loop[0]):
        loop.append((loop[0][0]+1, loop[0][1]))
    elif check_east(map=map, node=loop[0]):
        loop.append((loop[0][0], loop[0][1]+1))
    index=1
    # print(loop)
    while loop[0] != loop[-1]:
        current_node = loop[index]
        prev_node = loop[index-1]
        symbol = map[current_node[0]][current_node[1]]
        loop.append(get_next_node(current_symbol=symbol, current_node=current_node, prev_node=prev_node))
        # print(loop)
        index+=1
    answer = len(loop)//2
    return answer

if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)