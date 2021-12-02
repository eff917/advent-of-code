bagrules = {}

next_set = set()
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        line = line.strip()
        # print(line)
        head, tail = line.split(' bags contain ')
        bagrules[head] = tail
        # print(head)
        if "shiny gold" in tail:
            next_set.add(head)
can_contain = set()
while len(can_contain) < len(next_set):
    # print("running loop")
    can_contain = next_set.copy()
    for key, value in bagrules.items():
        for bag in can_contain:
            if bag in value:
                next_set.add(key)

# print(next_set)
print(len(next_set))