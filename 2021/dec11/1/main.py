from copy import deepcopy
url = '2021/dec11/input.txt'
# url = '2021/dec11/input-example.txt'

map = []
mapdict = {}
flashcount = 0
with open(url, 'r') as infile:
    for lineid, line in enumerate(infile):
        line = list(line.strip())
        map.append([int(x) for x in line])
        mapdict[lineid] = {}
        for xid, x in enumerate(line):
            mapdict[lineid][xid] = int(x)

for row in map:
    print(row)
print(f"Total flashes: {flashcount}")

def step(oldmap: list, flash_total: int):
    newmap = []
    flashed = set()
    # substep1: increase energy of all the octopi
    for row in oldmap:
        newmap.append([x+1 for x in row])
    # substep2: octopi with energy > 9 increase adjacent octopi energy by 1
    # this is recursive
    max_energy = 0
    for rowid, row in enumerate(newmap):
        for colid, col in enumerate(row):
            if (rowid, colid) not in flashed:
                max_energy = max(max_energy, col)

    while max_energy > 9:
        for rowid, row in enumerate(newmap):
            for colid, col in enumerate(row):
                if col > 9 and (rowid, colid) not in flashed:
                    for y in range(max(0, rowid -1), min(len(newmap), rowid+2)):
                        for x in range(max(0, colid-1), min(len(row), colid+2)):
                            newmap[y][x] += 1
                    flashed.add((rowid, colid))
        max_energy = 0
        for rowid, row in enumerate(newmap):
            for colid, col in enumerate(row):
                if (rowid, colid) not in flashed:
                    max_energy = max(max_energy, col)

    # substep3: reset flashed octopus energy to 0
    for y, x in flashed:
        newmap[y][x] = 0
    return(newmap, flash_total + len(flashed))



for i in range(100):
    print(f'Round {i+1}')
    map, flashcount = step(map, flashcount)
    for row in map:
        print(' '.join( [str(x) for x in row] ))
    print(f"Total flashes: {flashcount}\n")
