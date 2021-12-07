fileurl = '2021/dec8/input.txt'
# fileurl = '2021/dec8/input-example.txt'

with open(fileurl, 'r') as infile:
    for line in infile:
        positions = [int(x) for x in line.strip().split(',')]

# print(positions)
minpos = positions[0]
maxpos = positions[0]
for pos in positions:
    minpos = min(minpos, pos)
    maxpos = max(maxpos, pos)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fuel_consumed(distance: int):
    sum = 0
    for i in range(distance+1):
        sum += i
    return sum

# calculate fuel for each position from min to max
fuel_cost = {}
for i in range(minpos, maxpos+1):
    fuel_cost[i] = 0
    for crab in positions:
        if fuel_cost[i] <= min(fuel_cost.values()):
            fuel_cost[i] += fuel_consumed(abs(crab - i))
# print(fuel_cost)
print(min(fuel_cost.values()))
