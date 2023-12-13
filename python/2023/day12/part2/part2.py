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
        # try to cut off invalid branches
        # DONE
        # number of # > sum damages ()
        # #+? < sum damages (can't convert enough ? to #)
        # TODO
        # cut out matching parts? eg. .###. ,3,
        # try matching question marks at start, and reduce them eg .?###. and larged damaged block is 3

        line1 = f"{line[:index]}.{line[index+1:]}"
        if line1.count("#") <= sum(damages) and line1.count("#") + line1.count("?") >= sum(damages) and "#"*(max(damages)+1) not in line1:
            permutations += get_line_permutations(line1, damages)
        line2 = f"{line[:index]}#{line[index+1:]}"
        if line2.count("#") <= sum(damages) and line2.count("#") + line2.count("?") >= sum(damages) and "#"*(max(damages)+1) not in line2:
            permutations += get_line_permutations(line2, damages)
        return permutations

def unfold(map, damage_groups):
    new_map = []
    new_damage_groups = []
    for line in map:
        new_line = line
        for i in range(4):
            new_line += f"?{line}"
        new_map.append(new_line)
    for line in damage_groups:
        new_line = line*5
        new_damage_groups.append(new_line)
    return (new_map, new_damage_groups)


def main(infile):
    answer = 0
    map, damage_groups = parse_input(infile)
    map, damage_groups = unfold(map=map, damage_groups=damage_groups)
    for i in range(len(map)):
        answer += get_line_permutations(map[i], damage_groups[i])
        print(f"Line {i} out of {len(map)} done.")
    return answer


if __name__ == "__main__":
    infile = "input.txt"
    answer = main(infile)
    print(answer)
