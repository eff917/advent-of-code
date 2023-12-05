from copy import deepcopy
from collections import Counter
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


for i in range(10):
    new_polimer = []
    for idx, char in enumerate(template[1:]):
        # print(f"{idx, char}")
        new_polimer.append(template[idx])
        pair = ''.join([template[idx], char])
        if pair in polimers.keys():
            new_polimer.append(polimers[pair])
    new_polimer.append(char)
    template = deepcopy(new_polimer)
    print(f"{''.join(template)} {Counter(''.join(template))}")


charcount = Counter(template)

print(max(charcount.values()) - min(charcount.values()))