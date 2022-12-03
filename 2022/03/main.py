import os
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

# print(ord('a')-96)
# print(ord('A')-38)

def solution(infile):
    priosum1 = 0
    priosum2 = 0
    count = 0
    bags = ["", "", ""]
    for line in infile:
        if line[-1] == '\n':
            line = line[:-1]
        comp1 = set(line[0:len(line)//2])
        comp2 = set(line[len(line)//2::])
        item = comp1.intersection(comp2).pop()
        if item.islower():
            prio = ord(item) - 96
        else:
            prio = ord(item) - 38
        priosum1 += prio
        bags[count%3] = line
        if count%3 == 2:
            badge = (set(bags[0]).intersection(set(bags[1]).intersection(set(bags[2])))).pop()
            # print(badge)
            if badge.islower():
                prio = ord(badge) - 96
            else:
                prio = ord(badge) - 38
            # print(prio)
            priosum2 += prio

        count += 1
    print(f"Priority sum (part1): {priosum1}")
    print(f"Priority sum (part2): {priosum2}")



print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)
print("input.txt")
with open(infile, 'r') as infile:
    solution(infile)

