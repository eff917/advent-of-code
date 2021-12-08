fileurl = '2021/dec8/input.txt'
# fileurl = '2021/dec8/input-example.txt'

with open(fileurl, 'r') as infile:
    for line in infile:
        positions = [int(x) for x in line.strip().split(',')]

print(positions)
minpos = positions[0]
maxpos = positions[0]
for pos in positions:
    minpos = min(minpos, pos)
    maxpos = max(maxpos, pos)

# calculate fuel for each position from min to max
fuel_cost = {}
for i in range(minpos, maxpos+1):
    fuel_cost[i] = 0
    for crab in positions:
        fuel_cost[i] += abs(crab - i)
print(min(fuel_cost.values()))
