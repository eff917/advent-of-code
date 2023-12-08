import os
import math
import pprint

pp = pprint.PrettyPrinter(indent=2)


# region part2
part = "part2"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/test-input.txt"
summary = 0


def get_next_type_and_id(id_ranges: list, id: int):
    range_found = False
    next_target = ""
    for id_range in id_ranges:
        next_target = id_range["target"]
        if (
            id >= id_range["source_id"]
            and id <= id_range["source_id"] + id_range["range_value"]
        ):
            value = id + id_range["offset"]
            range_found = True
    if not range_found:
        value = id

    return (next_target, value)


map = {}
with open(infile) as file:
    for line in file:
        line = line.strip()
        # parse seeds
        if line.startswith("seeds: "):
            seeds = line.split(" ")[1:]
        # skip empty lines
        elif line == "":
            continue
        # parse map header
        elif "map" in line:
            source, _, target = line.split(" ")[0].split("-")
        # parse map ranges
        else:
            target_id, source_id, range_value = line.split(" ")
            offset = int(target_id) - int(source_id)
            # TODO change this to lists inside map[destination]
            if source not in map.keys():
                map[source] = {
                    "target": target,
                    "ranges": [
                        {
                            "range_start": int(source_id),
                            "range_end": int(source_id) + int(range_value)-1,
                            "offset": offset,
                        }
                    ],
                }
            else:
                map[source]["ranges"].append(
                    {
                        "range_start": int(source_id),
                        "range_end": int(source_id) + int(range_value)-1,
                        "offset": offset,
                    }
                )

id_map = []
for i in range(0, len(seeds), 2):
    id_map.append({
        "id_start": int(seeds[i]),
        "id_end": int(seeds[i])+int(seeds[i+1])-1
    })

pp.pprint(id_map)
pp.pprint(map['seed'])

print(f"Part2 answer: {summary}")
# endregion part2
