import sys
numbers = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        numbers.append(int(line))

for a in numbers:
    for b in numbers:
        if a+b == 2020 :
            print(a*b)
            sys.exit(0)