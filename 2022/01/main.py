import os
# part1
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
maxcalory1=0
maxcalory2=0
maxcalory3=0
calory = 0
with open(infile, 'r') as infile:
    for line in infile:
        if len(line) > 1:
            calory += int(line)
        else:
            print(calory)
            if calory > maxcalory1:
                maxcalory3 = maxcalory2
                maxcalory2 = maxcalory1
                maxcalory1 = calory
            elif calory > maxcalory2:
                maxcalory3 = maxcalory2
                maxcalory2 = calory
            elif calory > maxcalory3:
                maxcalory3 = calory
            calory = 0

print(calory)
if calory > maxcalory1:
    maxcalory3 = maxcalory2
    maxcalory2 = maxcalory1
    maxcalory1 = calory
elif calory > maxcalory2:
    maxcalory3 = maxcalory2
    maxcalory2 = calory
elif calory > maxcalory3:
    maxcalory3 = calory
calory = 0

print(f"Max calory (part1): {maxcalory1}")

print(maxcalory1, maxcalory2, maxcalory3)
print(f"Top 3 calory sum (part2): {maxcalory1+maxcalory2+maxcalory3}")