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

# print(lowpoints)
# print(lowpint_coords)
sum = 0
for x in lowpoints:
    sum += x+1
print(f"Sum of risk levels: {sum}")

print(f"Number of basins: {len(lowpoints)}")

basins = [ [x] for x in lowpint_coords]

for basin in basins:
    # print(basin)
    for rowid, columnid in basin:
        # print(rowid, columnid)
        # search down
        if rowid < len(map) -1:
            for i in range(rowid + 1, len(map)):
                if map[i][columnid] >= map[i-1][columnid] and map[i][columnid] < 9:
                    if [i, columnid] not in basin:
                        basin.append([i, columnid])
                else:
                    break
        # search up
        if rowid > 0:
            for i in range(rowid -1, -1, -1):
                if map[i][columnid] >= map[i+1][columnid] and map[i][columnid] < 9:
                    if [i, columnid] not in basin:
                        basin.append([i, columnid])
                else:
                    break
        # search right
        if columnid < len(map[0]) - 1:
            for j in range(columnid + 1, len(map[0])):
                if map[rowid][j] >= map[rowid][j-1] and map[rowid][j] < 9:
                    if [rowid, j] not in basin:
                        basin.append([rowid, j])
                else:
                    break
        # search left
        if columnid > 0:
            for j in range(columnid -1, -1, -1):
                if map[rowid][j] >= map[rowid][j+1] and map[rowid][j] < 9:
                    if [rowid, j] not in basin:
                        basin.append([rowid, j])
                else:
                    break
sizes = []
for basinid, basin in enumerate(basins):
    # print(f"Basin {basinid}")
    # print(f"size: {len(basin)}")
    sizes.append(len(basin))
    # print(basin)
sizes = sorted(sizes)
print(f"3 largest basin sizes: {sizes[-3:]}")
print(f"Produc of the 3 argest sies: {sizes[-1]*sizes[-2]* sizes[-3]}")