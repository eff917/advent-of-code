import os
import pprint

pp = pprint.PrettyPrinter(indent=2)


def parse_input(filename: str):
    path = f"{os.path.dirname(os.path.realpath(__file__))}/{filename}"
    map = []
    damage_groups = []
    with open(path) as file:
        for line in file:
            springs, damages = line.split()
            damages = damages.split(',')
            damages = list(int(damage) for damage in damages)
            map.append(springs)
            damage_groups.append(damages)
    return (map, damage_groups)

def get_damages(line):
    line = line.split(".")
    i=0
    while i< len(line):
        if "#" not in line[i]:
            del line[i]
        else:
            i+=1
    damages = []
    for damage in line:
        damages.append(len(damage))
    return damages
    
def get_line_permutations(line, damages):
    permutations = 0
    index = line.find("?")
    if index == -1:
        if get_damages(line) == damages:
            return 1
        else:
            return 0
    else:
        line1 = f"{line[:index]}.{line[index+1:]}"
        permutations += get_line_permutations(line1, damages)
        line2 = f"{line[:index]}#{line[index+1:]}"
        permutations += get_line_permutations(line2, damages)
        return permutations



def main(infile):
    answer = 0
    map, damage_groups = parse_input(infile)
    for i in range(len(map)):
        answer += get_line_permutations(map[i], damage_groups[i])
    return answer


if __name__ == "__main__":
    infile = "input.txt"
    answer = main(infile)
    print(answer)
