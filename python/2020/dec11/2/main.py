from copy import deepcopy
from os import truncate
map = []
with open('2020/dec11/input.txt', 'r') as inputfile:
    for line in inputfile:
        map.append(list(line.strip()))
    
def check_neighbours(mymap, rowidx, colidx):
    # TODO rewrite this to first seat
    # print(f"{rowidx} {colidx}")
    taken = 0
    # if colidx == 9:
    #     print(taken)
    # up
    has_neighbor = False
    i = 1
    while rowidx - i > -1:
        if mymap[rowidx - i][colidx] == '#':
            has_neighbor = True
            break
        elif mymap[rowidx - i][colidx] == 'L':
            break
        elif mymap[rowidx - i][colidx] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # down
    i = 1
    while rowidx + i < len(mymap):
        if mymap[rowidx + i][colidx] == '#':
            has_neighbor = True
            break
        elif mymap[rowidx + i][colidx] == 'L':
            break
        elif mymap[rowidx + i][colidx] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # left
    i = 1
    while colidx - i > -1:
        if mymap[rowidx][colidx - i] == '#':
            has_neighbor = True
            break
        elif mymap[rowidx][colidx - i] == 'L':
            break
        elif mymap[rowidx][colidx - i] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # right
    i = 1
    while colidx + i < len(mymap[0]):
        if mymap[rowidx][colidx + i] == '#':
            has_neighbor = True
            break
        elif mymap[rowidx][colidx + i] == 'L':
            break
        elif mymap[rowidx][colidx + i] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # diagonal up left
    i = 1
    while (rowidx - i) > -1 and (colidx - i) > -1:
        if mymap[rowidx - i][colidx - i] == '#':
            has_neighbor = True
            break
        elif mymap[rowidx - i][colidx - i] == 'L':
            break
        elif mymap[rowidx - i][colidx - i] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # diagonal up right
    i = 1
    while (rowidx - i) > -1 and (colidx + i) < len(mymap[0]):
        if mymap[rowidx - i][colidx + i] == '#':
            has_neighbor = True
        if mymap[rowidx - i][colidx + i] == 'L':
            break
        if mymap[rowidx - i][colidx + i] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # diagonal down left
    i = 1
    while (rowidx + i) < len(mymap) and (colidx - i) > -1:
        if mymap[rowidx + i][colidx - i] == '#':
            has_neighbor = True
            break
        if mymap[rowidx + i][colidx - i] == 'L':
            break
        if mymap[rowidx + i][colidx - i] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # diagonal up right
    i = 1
    while (rowidx + i) < len(mymap) and (colidx + i) < len(mymap[0]):
        if mymap[rowidx + i][colidx + i] == '#':
            has_neighbor = True
            break
        if mymap[rowidx + i][colidx + i] == 'L':
            break
        if mymap[rowidx + i][colidx + i] == '.':
            pass
        i += 1
    if has_neighbor:
        taken += 1
    has_neighbor = False
    # if colidx == 9:
    #     print(taken)
    # print("finished checking")
    return taken

def cycle(mmap):
    new_map = deepcopy(mmap)
    # print("starting cycle")
    for rowid, row in enumerate(mmap):
        # print(f"checking row {rowid}")
        for colid, col in enumerate(row):
            # print(f"checking column {colid}")
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
                if taken > 4:
                    new_map[rowid][colid] = 'L'
    return new_map



new_map = deepcopy(map)
for line in new_map:
    print(''.join(line))
print()
old_map = []
while new_map != old_map:
    old_map = deepcopy(new_map)
    new_map = cycle(old_map)
    for line in new_map:
        print(''.join(line))
    print()


count = 0
for line in new_map:
    for char in line:
        if char == "#":
            count += 1

print(count)
