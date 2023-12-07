import os
import math

# region part1
part = "part1"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"
summary = 0
map = {}
with open(infile) as file:
    for line in file:
        line = line.strip()
        if line.startswith("seeds: "):
            seeds = line.split(" ")[1:]
        elif line == '':
            continue
        elif 'map' in line:
            source, _, target = line.split(' ')[0].split('-')
        else:
            target_id, source_id,  range_value = line.split(' ')
            offset = int(target_id) - int(source_id)
            # TODO change this to lists inside map[destination]
            if source not in map.keys():
                map[source] = [{"target": target, "source_id": int(source_id), "offset": offset, "range_value": int(range_value)}]
            else:
                map[source].append({"target": target, "source_id": int(source_id), "offset": offset, "range_value": int(range_value)})
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

target = "seed"
next_target = map["seed"][0]["target"]
id_map = {}
for seed in seeds:
    id_map[seed] = {"seed": seed}
while next_target in map.keys():
    for line in id_map.values():
        seed = line[target]
        range_found = False
        for ranges in map[target]:
            next_target = ranges["target"]
            if seed in range(ranges["source_id"], ranges["source_id"]+ranges["range_value"]):
                value = seed + ranges["offset"]
                range_found = True
        if not range_found:
            value = seed
        id_map[line["seed"]][next_target] = value
        # print(f"{target} value is {value} for seed {seed}")
    target = next_target
# print(seeds)
# print(id_map)
minimum_location_id = None
for key, value in id_map.items():
    # print(f"{key}: {value}")
    if minimum_location_id is None:
        minimum_location_id = value["location"]
    if value["location"] < minimum_location_id:
        minimum_location_id = value["location"]
summary = minimum_location_id

print(f"Part1 answer: {summary}")



# endregion part1

# region part2
part = "part2"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/test-input.txt"
summary = 0
def get_next_type_and_id(id_ranges: list, id: int):
    range_found = False
    next_target = ''
    for id_range in id_ranges:
        next_target = id_range["target"]
        if id >= id_range["source_id"] and id <= id_range["source_id"]+id_range["range_value"]:
            value = id + id_range["offset"]
            range_found = True
    if not range_found:
        value = id

    return (next_target, value)
map = {}
with open(infile) as file:
    for line in file:
        line = line.strip()
        if line.startswith("seeds: "):
            seeds = line.split(" ")[1:]
        elif line == '':
            continue
        elif 'map' in line:
            source, _, target = line.split(' ')[0].split('-')
        else:
            target_id, source_id,  range_value = line.split(' ')
            offset = int(target_id) - int(source_id)
            # TODO change this to lists inside map[destination]
            if source not in map.keys():
                map[source] = [{"target": target, "source_id": int(source_id), "offset": offset, "range_value": int(range_value)}]
            else:
                map[source].append({"target": target, "source_id": int(source_id), "offset": offset, "range_value": int(range_value)})

# convert seed ids to int
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])


# TODO calculate location on a per seed basis
min_location = None
for i in range(0, len(seeds), 2):
    for j in range(seeds[i+1]):
        seed = seeds[i] + j
        id = seed
        # reset target to seed
        target = "seed"
        while target != 'location':
            target, id = get_next_type_and_id(map[target], id)
        if min_location is None:
            min_location = id
        min_location = min(id, min_location)
        # print(f"{seed} {target} is {id}")
    print(f"{i} done")

summary = min_location
print(f"Part2 answer: {summary}")
# endregion part2
