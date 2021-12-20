from copy import deepcopy
from os import readlink
url = '2021/dec14/input.txt'
url = '2021/dec14/input-example.txt'


polimers = {}
polimers[2] = {}
with open(url, 'r') as infile:
    template = infile.readline().strip()
    infile.readline()
    rule = infile.readline().strip().split(' -> ')
    while len(rule) > 1:
        # add the first char of the source to the target
        polimers[2][rule[0]]= rule[0][0] + rule[1]
        rule = infile.readline().strip().split(' -> ')


# example runtime with list:
# 10 loops: 0.5s
# 20 loops: 4.6s
# 21 loops: 9.3s
# 22 loops: 16.446s
# 23 loops: 34.163s

# example runtimes with string:
# 20 loops:  1.981s
# 21 loops:  4.930s
# 22 loops:  7.395s
# 23 loops: 15.583s
# 24 loops: 31.695s
# 25 loops: ~1minute
# only halved the runtime, it would take ~ 2^15 minutes to run 40 loops ~546hours

# runtimes with less operations (added char to rule result, instead of adding chars separately)
# 20 loops: example  1.335s full  6.411s
# 21 loops: example   1.895s full 12.223s
# 22 loops: example   3.903s full 22.628s
# 23 loops: example   7.547s full 44.531s
# 24 loops: example  14.155s full - 
# 25 loops: example  27.538s full -
# 26 loops: example  54.910s full -
# 27 loops: exmaple 118.695s full -

# time to start memoization, and building a library of bigger chunks.

import time
t0 = time.time()

for i in range(27):
    new_polimer = ''
    first_char = template[0]
    old_polimer = template[0]
    for char in template[1:]:
        new_polimer += polimers[2][first_char + char]
        first_char = char
    new_polimer += char
    template = new_polimer
    print(f"Finished round {i+1} in {time.time() - t0} seconds. Length: {len(template)}")


charset = set(template)
print(charset)

charcount = {}

for char in charset:
    print(f"{char}: {template.count(char)}")
    charcount[char] = template.count(char)


print(max(charcount.values()) - min(charcount.values()))