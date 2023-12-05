with open("../input.txt") as file:
    data = [int(line) for line in file]

data.insert(0, 0)  # Power outlet
data.append(max(data) + 3)  # Device
data.sort()

count = {0: 1}  # Counts the ways to reach each adapter

for adapter in data[1:]:  # Skip the first adapter (charging outlet - 0)
    # The number of ways to reach is the sum of the number of ways
    # to reach the three previous adapters (those that exist)
    count[adapter] = count.get(adapter-1, 0) + count.get(adapter-2, 0) + count.get(adapter-3, 0)

part2 = count[data[-1]]  # Take the number of ways to reach the device (last adapter)
print(part2)