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
    print(positions)
    instruction_length = len(instructions)
    # pp.pprint(f"Map:\n{map}")
    # print(instructions)
    steps_to_arrive = []
    steps_to_loop = []
    loop_stepcount = []
    print(f"Positions: {positions}")
    answer = 0
    for sposition in positions:
        position = sposition
        arrived = 0
        i = 0
        while position[-1] != 'Z' or arrived < 2:
            position = step(position=position, instruction=instructions[i%instruction_length], map=map[position])
            print(f"{sposition} {position} {i}")
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

    p_count = len(positions)
    for i in range(p_count):
        loop_stepcount.append(steps_to_loop[i]-steps_to_arrive[i])

    x = steps_to_arrive[0]
    step_value = loop_stepcount[0]
    found = False

    print(f"Inital steps required: {steps_to_arrive}")
    print(f"Steps in loop        : {loop_stepcount}")

    lcm = math.lcm(loop_stepcount[0], loop_stepcount[1])
    for i in range(2,p_count):
        lcm = math.lcm(lcm, loop_stepcount[i])
    print(f"Least common multiple = {lcm}")

    answer = lcm
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    answer = main(infile)
    print(answer)

