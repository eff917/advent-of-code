from copy import deepcopy
from os import readlink
url = '2021/dec14/input.txt'
url = '2021/dec14/input-example.txt'


polimers = {}
with open(url, 'r') as infile:
    template = list(infile.readline().strip())
    infile.readline()
    rule = infile.readline().strip().split(' -> ')
    while len(rule) > 1:
        polimers[rule[0]]= rule[1]
        rule = infile.readline().strip().split(' -> ')


# example runtime:
# 10 loops: 0.5s
# 20 loops: 4.6s
# 21 loops: 9.3s
# 22 loops: 16.446s
for i in range(22):
    new_polimer = []
    first_char = template[0]
    for idx, char in enumerate(template[1:]):
        # print(f"{idx, char}")
        new_polimer.append(first_char)
        pair = f"{first_char}{char}"
        if pair in polimers.keys():
            new_polimer.append(polimers[pair])
        first_char = char
    new_polimer.append(char)
    template = deepcopy(new_polimer)
    # print(''.join(template))


charset = set(template)
print(charset)

charcount = {}

for char in charset:
    print(f"{char}: {template.count(char)}")
    charcount[char] = template.count(char)


print(max(charcount.values()) - min(charcount.values()))