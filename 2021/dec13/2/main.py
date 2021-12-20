from copy import deepcopy
url = '2021/dec13/input.txt'
# url = '2021/dec13/input-example.txt'

dots = set()
folds = []
with open(url, 'r') as infile:
    line = infile.readline().strip()
    while len(line) > 0:
        x, y = line.split(',')
        dots.add((int(x), int(y)))
        line = infile.readline().strip()
    line = infile.readline().strip().split(' ')
    while len(line) > 1:
        fold = line[2].split('=')
        fold[1] = int(fold[1])
        folds.append(fold)
        line = infile.readline().strip().split(' ')
        
print(dots)    
print(folds)

def fold(coordinate, fold_coordinate):
    if coordinate < fold_coordinate:
        return coordinate
    else:
        return fold_coordinate + fold_coordinate - coordinate

for fold_direction, fold_coordinate in folds:
    new_dots = set()
    for x_coord, y_coord in dots:
        if fold_direction == 'y':
            new_dots.add((x_coord, fold(y_coord, fold_coordinate)))
        elif fold_direction == 'x':
            new_dots.add((fold(x_coord, fold_coordinate), y_coord))
    dots = deepcopy(new_dots)
    print(len(new_dots))
print(dots)

max_x = 0
max_y = 0
for x, y in dots:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

map = []

for j in range(max_y+1):
    line = ''
    for i in range(max_x+1):
        line += '.'
    line = list(line)
    map.append(line)

for line in map:
    print(''.join(line))

print(dots)
for x, y in dots:
    print(f"setting {y}, {x}")
    map[y][x] = '#'

for line in map:
    print(''.join(line))
