import sys
numbers = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        numbers.append(int(line))

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a+b+c == 2020 :
                print(a*b*c)
                sys.exit(0)