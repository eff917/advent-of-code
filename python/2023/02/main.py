import os

part = "part1"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"

valid_game_sum = 0
limits = {"red": 12, "green": 13, "blue": 14}
with open(infile) as infile:
    for line in infile:
        game_is_valid = True
        game_id, game = line.split(":")
        game_id = int(game_id.split(" ")[-1])
        turns = game.strip().split(';')
        for turn_id, turn in enumerate(turns):
            if game_is_valid:
                cubes = turn.strip().split(',')
                for cube in cubes:
                    cube_number, cube_colour = cube.strip().split(' ')
                    print(f"{game_id}, {turn_id}: {cube_number}, {cube_colour} cubes")
                    if int(cube_number) > limits[cube_colour]:
                        game_is_valid = False
            else:
                break
        if game_is_valid:
            valid_game_sum += game_id
print(valid_game_sum)
                    



part = "part2"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"

with open(infile) as infile:
    for line in infile:
        pass
