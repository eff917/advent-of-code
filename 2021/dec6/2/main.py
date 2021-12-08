fishlist = []
fishdict = {}
with open('2021/dec7/input.txt', 'r') as infile:
    for line in infile:
        fishlist = line.strip().split(',')
        fishlist = [int(x) for x in fishlist]
        for fish in fishlist:
            if fish in fishdict.keys():
                fishdict[fish] += 1
            else:
                fishdict[fish] = 1

print(fishdict)

def dictcycle(inputdict):
    nextdict = {}
    for key, value in inputdict.items():
        nextdict[key -1 ] = value
    if -1 in nextdict.keys():
        nextdict[8] = nextdict[-1]
        if 6 in nextdict.keys():
            nextdict[6] += nextdict[-1]
        else:
            nextdict[6] = nextdict[-1]
        del nextdict[-1]
    return nextdict


for i in range(256):
    fishdict = dictcycle(fishdict)
    print(fishdict)
sum = 0
for value in fishdict.values():
    sum += value
print(sum)