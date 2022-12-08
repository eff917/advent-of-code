import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    map = []
    visible_count = 0
    max_scenic_score = 0
    for line in infile:
        line = line.strip()
        map.append(line)
    for x in range(len(map[0])):
        for y in range(len(map)):
            if is_visible(x, y, map):
                visible_count += 1
            max_scenic_score = max(scenic_score(x, y, map), max_scenic_score)
    print(f"Part1: {visible_count}")
    print(f"Part2: {max_scenic_score}")
    

def is_visible(x, y, map):
    is_visible_from_left = True
    is_visible_from_right = True
    is_visible_from_top = True
    is_visible_from_bottom = True
    # left to right
    for tree in map[y][:x]:
        if tree >= map[y][x]:
            is_visible_from_left = False
    # right to left
    for tree in map[y][:x:-1]:
        if tree >= map[y][x]:
            is_visible_from_right = False
    # top down
    for trees in map[:y]:
        if trees[x] >= map[y][x]:
            is_visible_from_top = False
    # bottom up
    for trees in map[:y:-1]:
        if trees[x] >= map[y][x]:
            is_visible_from_bottom = False
    return is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom

def scenic_score(x, y, map):
    scenic_score_left = 0
    scenic_score_right = 0
    scenic_score_top = 0
    scenic_score_bottom = 0
    print(f"\nChecking x: {x}, y: {y}")
    # left to right
    for tree in map[y][x+1:]:
        print(f"checking to right: {tree} against {map[y][x]}")
        if tree < map[y][x]:
            scenic_score_left += 1
        else:
            scenic_score_left += 1
            break
    for tree in list(reversed(map[y]))[len(map[y]) - x:]:
        print(f"checking to left: {tree} against {map[y][x]}")
        if tree < map[y][x]:

            scenic_score_right += 1
        else:
            scenic_score_right += 1
            break
    for trees in map[y+1:]:
        print(f"checking to down: {trees[x]} against {map[y][x]}")
        if trees[x] < map[y][x]:
            scenic_score_top += 1
        else:
            scenic_score_top += 1
            break
    for trees in list(reversed(map))[len(map) - y:]:
        print(f"checking to up: {trees[x]} against {map[y][x]}")
        if trees[x] < map[y][x]:
            scenic_score_bottom += 1
        else:
            scenic_score_bottom += 1
            break
    print(f"Scenic score: {scenic_score_left}*{scenic_score_right}*{scenic_score_top}*{scenic_score_bottom}")
    return scenic_score_left * scenic_score_right * scenic_score_top * scenic_score_bottom


print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("Real")
with open(infile, 'r') as infile:
    solution(infile)
