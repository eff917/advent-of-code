import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile_example2 = f"{os.path.dirname(os.path.realpath(__file__))}/input-example2.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    moves = ''
    for line in infile:
        direction, count = line.split()
        for i in range(int(count)):
            moves += direction
    # print(moves)
    head_coords = [[0,0]]
    knot1_coords = [[0,0]]
    knot2_coords = [[0,0]]
    knot3_coords = [[0,0]]
    knot4_coords = [[0,0]]
    knot5_coords = [[0,0]]
    knot6_coords = [[0,0]]
    knot7_coords = [[0,0]]
    knot8_coords = [[0,0]]
    knot9_coords = [[0,0]]
    tail_coords = [[0,0]]
    for move in moves:
        if move == 'R':
            head_coords.append([head_coords[-1][0]+1,head_coords[-1][1]])
        elif move == 'L':
            head_coords.append([head_coords[-1][0]-1,head_coords[-1][1]])
        elif move == 'U':
            head_coords.append([head_coords[-1][0],head_coords[-1][1]+1])
        elif move == 'D':
            head_coords.append([head_coords[-1][0],head_coords[-1][1]-1])

        knot1_coords.append(move_knot(head_coords[-1], knot1_coords[-1]))
        knot2_coords.append(move_knot(knot1_coords[-1], knot2_coords[-1]))
        knot3_coords.append(move_knot(knot2_coords[-1], knot3_coords[-1]))
        knot4_coords.append(move_knot(knot3_coords[-1], knot4_coords[-1]))
        knot5_coords.append(move_knot(knot4_coords[-1], knot5_coords[-1]))
        knot6_coords.append(move_knot(knot5_coords[-1], knot6_coords[-1]))
        knot7_coords.append(move_knot(knot6_coords[-1], knot7_coords[-1]))
        knot8_coords.append(move_knot(knot7_coords[-1], knot8_coords[-1]))
        tail_coords.append(move_knot(knot8_coords[-1], tail_coords[-1]))

        

    # print(head_coords)
    # print(knot1_coords)
    # print(tail_coords)
    knot1_set = set()
    for coords in knot1_coords:
        knot1_set.add(f"{coords[0]},{coords[1]}")
    tail_set = set()
    # print(tail_set)
    for coords in tail_coords:
        tail_set.add(f"{coords[0]},{coords[1]}")
    print(f"Part1: {len(knot1_set)}")
    print(f"Part2: {len(tail_set)}")

def move_knot(head, tail):
    tail0 = tail[0]
    tail1 = tail[1]
    # moving left or right
    if abs(head[0] - tail[0]) > 1:
        # print("Moving left or right")
        tail0 = tail[0] + (head[0] - tail[0])//2
        # multiply by 1.1 so round(1/2) becomes 1
        tail1 = tail[1] + round((head[1] - tail[1])/2*1.1)
    # moving up or down
    elif abs(head[1] - tail[1]) > 1:
        # print("Moving up or down")
        tail1 = tail[1] + (head[1] - tail[1])//2
        # multiply by 1.1 so round(1/2) becomes 1
        tail0 = tail[0] + round((head[0] - tail[0])/2*1.1)
    # print(head, tail, tail0, tail1)
    return[tail0, tail1]
    




print("\nExample")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("\nExample2")
with open(infile_example2, 'r') as infile_example:
    solution(infile_example)

print("\nReal")
with open(infile, 'r') as infile:
    solution(infile)
