adapters = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        adapters.append(int(line.strip()))
adapters.sort()

differences = {}

# print(adapters)
# add socket
adapters.insert(0, 0)

prev = 0
for rating in adapters:
    difference = rating - prev
    if difference in differences.keys():
        differences[difference] +=1
    else:
        differences[difference] = 1
    prev = rating
# remove initial loop
del differences[0]
# add difference to device
differences[3] += 1
print(differences)
print(differences[1] * differences[3])
