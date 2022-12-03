import os
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

# A,X - Rock 1
# B,Y - Paper 2
# C,Z - Scissors 3
# 6 - win, 3 - draw, 0 loss
# print(ord("X"))


def roundpoints1(first, second):
    second = chr(ord(second) - 23)
    if first == second:
        return 3
    elif (first == "A" and second == "B") or (first == "B" and second == "C") or (first == "C" and second == "A"):
        return 6
    else:
        return 0

def roundpoints2(first, second):
    # draw
    if second == "Y":
        return ord(first)-ord("A")+1
    # loose
    if second == "X":
        if first == "A":
            return 3
        elif first == "B":
            return 1
        else:
            return 2
    # win
    else:
        if first == "A":
            return 2
        elif first == "B":
            return 3
        else:
            return 1


def solution(infile):
    points1 = 0
    points2 = 0
    with open(infile, 'r') as infile:
        for line in infile:
            # part1
            points1 += roundpoints1(line[0], line[2])
            points1 += ord(line[2])-87
            # part2            
            points2 += (ord(line[2])-88)*3
            points2 += roundpoints2(line[0], line[2])

        print(f"Points (Part1): {points1}")
        print(f"Points (Part2): {points2}")
print("Example")
solution(infile_example)
print("input.txt")
solution(infile)

