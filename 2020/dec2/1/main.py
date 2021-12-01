valid = 0
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        splitline = line.split(' ')
        min, max = splitline[0].split('-')
        count = splitline[2].count(splitline[1][0])
        print(min, max, splitline[1][0], splitline[2])
        if count <= int(max) and count >= int(min):
            valid += 1
print(valid)

