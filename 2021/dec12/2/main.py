from copy import deepcopy
from os import path
url = '2021/dec12/input.txt'
# url = '2021/dec12/input-example-3.txt'


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

# takes 22 minutes
for path in paths:
    # print(path)
    for edge in edges:
        # there is an edge connecting from the last node of the path, and it's not start or end
        if path[-1] in edge and path[-1] not in ['start', 'end']:
            # the edge is not reversed in the list
            if edge[0] == path[-1]:
                # if it's small, then check if we already went through it
                if edge[1].islower():
                    # new cave
                    if edge[1] not in path:
                        newpath = deepcopy(path)
                        newpath.append(edge[1])
                        paths.append(newpath)
                    # we have already visited this small cave
                    else:
                        # check if there's already a small cave in the path twice.
                        double_small_cave = False
                        for cave in path:
                            if path.count(cave) == 2 and cave.islower():
                                # there's already a small cave visited twice
                                double_small_cave = True
                                break
                        # no double visited small cave yet, we can visit this one again.
                        if not double_small_cave:
                            newpath = deepcopy(path)
                            newpath.append(edge[1])
                            paths.append(newpath)
                else:
                    newpath = deepcopy(path)
                    newpath.append(edge[1])
                    paths.append(newpath)
            # the edge is reversed in the list
            elif edge[1] == path[-1]:
                if edge[0].islower():
                    if edge[0] not in path:
                        newpath = deepcopy(path)
                        newpath.append(edge[0])
                        paths.append(newpath)
                    else:
                        # check if there's already a small cave in the path twice.
                        double_small_cave = False
                        for cave in path:
                            if path.count(cave) == 2 and cave.islower():
                                double_small_cave = True
                                # we found a small cave visited twice, no more allowed, stop checking
                                break
                        if not double_small_cave:
                            newpath = deepcopy(path)
                            newpath.append(edge[0])
                            paths.append(newpath)
                else:
                    newpath = deepcopy(path)
                    newpath.append(edge[0])
                    paths.append(newpath)
            # the edge is not connecting to the end of out path
            else:
                pass


count = 0

unique_paths = []
for path in paths:
    if path not in unique_paths:
        unique_paths.append(path)

unique_paths.sort()
for path in unique_paths:
    if path[-1] == 'end':
        count += 1
        print(','.join(path))

print(count)