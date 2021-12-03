from copy import deepcopy
map = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        map.append(list(line.strip()))
    
def check_neighbours(mymap, rowidx, colidx):
    taken = 0
    for nrow in range(rowidx-1, rowidx+2):
        for ncol in range(colidx-1, colidx+2):
            if nrow == -1 or nrow == len(mymap):
                continue
            elif ncol == -1 or ncol == len(mymap[0]):
                continue
            else:
                if mymap[nrow][ncol] == "#":
                    taken += 1
    # if the seat is taken, decrease, as we added it in the cycle above
    if mymap[rowidx][colidx] == "#":
        taken -= 1
    return taken

def cycle(mmap):
    new_map = deepcopy(mmap)

    for rowid, row in enumerate(mmap):
        for colid, col in enumerate(row):
            if col == ".":
                # floor, nothing changes
                pass
            elif col == "L":
                # free seat, if taken is 0, becomes occuiped
                taken = check_neighbours(mmap, rowid, colid)
                if taken == 0:
                    new_map[rowid][colid] = '#'
                    # top or bottom line:
            elif col == "#":
                # taken seat, if taken > 3, becomes empty
                taken = check_neighbours(mmap, rowid, colid)
                if taken > 3:
                    new_map[rowid][colid] = 'L'
    return new_map



new_map = deepcopy(map)
old_map = []
while new_map != old_map:
    old_map = deepcopy(new_map)
    new_map = cycle(old_map)

count = 0
for line in new_map:
    for char in line:
        if char == "#":
            count += 1

print(count)
