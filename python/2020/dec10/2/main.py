from typing import Counter


adapters = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        adapters.append(int(line.strip()))

# add socket
adapters.append(0)
# add device
adapters.append(max(adapters) + 3)
# sort adapters
adapters.sort()

# the number of ways to reach the adapter
path_count = {}

# we have a socket
path_count[0] = 1

# iterate over each adapter we have
for adapter in adapters[1:]:
    # the number of paths to reach our adapter is equal to
    # the sum of paths to reach the -1 -2 and -3 jolt rated adapters if they exist
    path_count[adapter] = path_count.get(adapter-1, 0) + path_count.get(adapter-2, 0) + path_count.get(adapter-3, 0)
# the last one (-1) is our device
print(path_count[adapters[-1]])