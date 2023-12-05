url = '2021/dec9/input.txt'
# url = '2021/dec9/input-example.txt'

map = []
with open(url, 'r') as infile:
    for line in infile:
        line = list(line.strip())
        map.append([int(x) for x in line])

# for line in map:
#     print(line)

lowpoints = []
lowpint_coords = []

for rowid, row in enumerate(map):
    for cellid, cell in enumerate(row):
        lower_neighbors = 0
        level_neighbors = 0
        higher_neighbors = 0
        if rowid > 0:
            if map[rowid -1][cellid] < cell:
                lower_neighbors += 1
            elif map[rowid -1][cellid] == cell:
                level_neighbors += 1
            else:
                higher_neighbors += 1
        if cellid > 0:
            if map[rowid][cellid -1] < cell:
                lower_neighbors += 1
            elif map[rowid][cellid -1] == cell:
                level_neighbors += 1
            else:
                higher_neighbors += 1
        try:
            if map[rowid +1][cellid] < cell:
                lower_neighbors += 1
            elif map[rowid +1][cellid] == cell:
                level_neighbors += 1
            else:
                higher_neighbors += 1
        except IndexError:
            pass
        try:
            if map[rowid][cellid + 1] < cell:
                lower_neighbors += 1
            elif map[rowid][cellid + 1] == cell:
                level_neighbors += 1
            else:
                higher_neighbors += 1
        except IndexError:
            pass
        if lower_neighbors == 0 and higher_neighbors > 0:
            lowpoints.append(cell)
            lowpint_coords.append([rowid, cellid])

print(lowpoints)
# print(lowpint_coords)
sum = 0
for x in lowpoints:
    sum += x+1

print(sum)