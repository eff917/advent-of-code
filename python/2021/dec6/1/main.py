fishlist = []
with open('2021/dec7/input.txt', 'r') as infile:
    for line in infile:
        fishlist = line.strip().split(',')
        fishlist = [int(x) for x in fishlist]

print(fishlist)

def cycle():
    for i in range(len(fishlist)):
        if fishlist[i] < 7:
            fishlist[i] = (fishlist[i] -1)%7
            if fishlist[i] == 6:
                fishlist.append(8)
        else:
            fishlist[i] = (fishlist[i] -1)

for i in range(80):
    cycle()
    print(len(fishlist))