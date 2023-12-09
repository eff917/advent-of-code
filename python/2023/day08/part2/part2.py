import os
import pprint
import math

pp = pprint.PrettyPrinter(indent=2)

def parse_input(path: str):
    map = {}
    with open(path) as file:
        for line in file:
            line = line.split()
            if len(line)==1:
                instructions = line[0]
            elif len(line) == 4:
                node = line[0]
                left = line[2][1:4]
                right = line[3][0:3]
                map[node] = {"L": left, "R": right}
    return (instructions, map)

def step(position, instruction, map):
    return map[instruction]

def arrived(positions):
    for position in positions:
        if position[-1] != "Z":
            return False
    return True

def main(infile):
    instructions, map = parse_input(infile)
    positions = list(filter(lambda x: (x[-1] == "A"), map.keys()))  
    i = 0
    print(positions)
    instruction_length = len(instructions)
    # pp.pprint(f"Map:\n{map}")
    # print(instructions)
    steps_to_arrive = []
    steps_to_loop = []
    loop_stepcount = []
    print(f"Positions: {positions}")
    answer = 0
    for position in positions:
        arrived = 0
        while position[-1] != 'Z' or arrived < 2:
            position = step(position=position, instruction=instructions[i%instruction_length], map=map[position])
            i += 1
            if position[-1] == 'Z':
                if arrived == 0:
                    steps_to_arrive.append(i)
                    print(f"{arrived}: {i}")
                    arrived +=1
                elif arrived == 1:
                    steps_to_loop.append(i)
                    arrived += 1
        print(f"{i} steps required for {position}")
    answer = i

    for i in range(len(positions)):
        print(f"Steps to arrive:{steps_to_arrive[i]}, loop: {steps_to_loop[i]-steps_to_arrive[i]}")
        loop_stepcount.append(steps_to_loop[i]-steps_to_arrive[i])

    #TODO find a number which is equal to a+b*N for each path
    # 17141 + 17141*N1
    # 53109 + 18827*N2
    # 92449 + 20513*N3
    # etc.
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)


# answers:
# 1: 17141
# 2: 1148447
# 3: 83836631

