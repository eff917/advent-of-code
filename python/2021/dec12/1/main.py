from copy import deepcopy
from os import path
url = '2021/dec12/input.txt'
# url = '2021/dec12/input-example.txt'


edges = []
with open(url, 'r') as infile:
    for line in infile:
        edges.append(line.strip().split('-'))

# print(edges)

paths = []
# first step 
for edge in edges:
    if 'start' in edge:
        if edge[0] == 'start':
            paths.append([edge[0], edge[1]])
        else:
            paths.append([edge[1], edge[0]])
# print(paths)

for path in paths:
    # print(path)
    for edge in edges:
        # there is an edge connecting from the last node of the path, and it's not end
        if path[-1] in edge and path[-1] != 'end':
            # the edge is not reversed in the list
            if edge[0] == path[-1]:
                # if it's small, then check if we already went through it
                if edge[1].islower():
                    if edge[1] not in path:
                        newpath = deepcopy(path)
                        newpath.append(edge[1])
                        paths.append(newpath)
                else:
                    newpath = deepcopy(path)
                    newpath.append(edge[1])
                    paths.append(newpath)
            # the edge is not reversed in the list
            else:
                if edge[1] == path[-1]:
                    if edge[0].islower():
                        if edge[0] not in path:
                            newpath = deepcopy(path)
                            newpath.append(edge[0])
                            paths.append(newpath)
                    else:
                        newpath = deepcopy(path)
                        newpath.append(edge[0])
                        paths.append(newpath)

for path in paths:
    print(path)

count = 0

for path in paths:
    if path[-1] == 'end':
        count += 1

print(count)