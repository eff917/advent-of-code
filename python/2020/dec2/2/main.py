valid = 0
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        splitline = line.split(' ')
        min, max = splitline[0].split('-')
        first = (splitline[2][int(min) -1] == splitline[1][0])
        second = (splitline[2][int(max) -1] == splitline[1][0])
        if first and not second:
            valid += 1
        if second and not first:
            valid +=1
print(valid)

