import os
import math
import pprint
import typing

pp = pprint.PrettyPrinter(indent=2)

# region part2


def parse_input(path: str):
    map = {}
    with open(path) as file:
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
                                "range_end": int(source_id) + int(range_value) - 1,
                                "offset": offset,
                            }
                        ],
                    }
                else:
                    map[source]["ranges"].append(
                        {
                            "range_start": int(source_id),
                            "range_end": int(source_id) + int(range_value) - 1,
                            "offset": offset,
                        }
                    )

    return (map, seeds)

    """convert an id range into the reange(s) of the next resource type based on a list of ranges
    """


def convert_range_to_next(ranges: list, id_range: dict) -> list:
    # id_ranges that have been processed and offset to the next resource type
    processed_ranges = []
    unprocessed_ranges = [id_range]
    while len(unprocessed_ranges) > 0:
        unprocessed_range = unprocessed_ranges.pop()
        id_range_start = unprocessed_range["id_start"]
        id_range_end = unprocessed_range["id_end"]
        for index, range in enumerate(ranges):
            range_start = range["range_start"]
            range_end = range["range_end"]
            offset = range["offset"]
            # cases:
            # 1: id_range is fully inside, convert, break (we're done)
            #    (range_start <= start <= end <= range_end)
            if range_start <= id_range_start <= id_range_end <= range_end:
                processed_ranges.append(
                    {
                        "id_start": id_range_start + offset,
                        "id_end": id_range_end + offset,
                    }
                )
                break
            # 2: id_range is outside of this range, continue, unless this is the last rule
            #    (end < range_start or start > range_end)
            if id_range_end < range_start or range_end < id_range_start:
                if index < len(ranges) - 1:
                    continue
                else:
                    processed_ranges.append(
                        {
                            "id_start": id_range_start,
                            "id_end": id_range_end,
                        }
                    )
                    break
            # 3: id_range starts before range, but ends inside range: split into 2, check outside part against other ranges
            #    (start < range_start <= end <= range_end)
            if id_range_start < range_start <= id_range_end <= range_end:
                processed_ranges.append(
                    {"id_start": range_start + offset, "id_end": id_range_end + offset}
                )
                unprocessed_ranges.append(
                    {"id_start": id_range_start, "id_end": range_start - 1}
                )
                break
                # we removed the current range from unporocessed
                break
            #    inside part goes into processed_ranges, outside part goes into id_range
            # 4: id_range starts inside range, but ends outside: split into 2, check outside part against other ranges
            #    (range_start <= start <= range_end < end)
            if range_start <= id_range_start <= range_end < id_range_end:
                processed_ranges.append(
                    {"id_start": id_range_start + offset, "id_end": range_end + offset}
                )
                unprocessed_ranges.append(
                    {"id_start": range_end + 1, "id_end": id_range_end}
                )
                break
            #    inside part goes into processed_ranges, outside part goes into id_range
            # 5: id_range is bigger than range: split into 3, check outside parts against other ranges
            #    (start < range_start <= range_end < end)
            #    inside part goes into processed_ranges, outside part goes into id_range (TODO this is a special case as it becomes 2 ranges)
            if id_range_start < range_start <= range_end < id_range_end:
                processed_ranges.append(
                    {"id_start": range_start + offset, "id_end": range_end + offset}
                )
                unprocessed_ranges.append(
                    {"id_start": id_range_start, "id_end": range_start - 1}
                )
                unprocessed_ranges.append(
                    {"id_start": range_end + 1, "id_end": id_range_end}
                )
                break
        # if processed_ranges is is empty, then return the same, because the default rule is id doesn't change

    return processed_ranges


def main(infile):
    part = "part2"
    summary = 0
    map, seeds = parse_input(infile)

    # convert seed list to ranges with start and end
    id_map = { "seed": []}
    for i in range(0, len(seeds), 2):
        id_map["seed"].append(
            {"id_start": int(seeds[i]), "id_end": int(seeds[i]) + int(seeds[i + 1]) - 1}
        )
    rtype = "seed"
    print(map[rtype])
    print(id_map)

    while rtype != 'location':
        next_rtype = map[rtype]["target"]
        for id_range in id_map[rtype]:

            if  next_rtype not in id_map.keys():
                id_map[next_rtype] = []
            ranges = convert_range_to_next(map[rtype]["ranges"], id_range)
            id_map[next_rtype] += ranges

            # print(ranges)
        rtype = map[rtype]["target"]

    pp.pprint(id_map)
    min_location = None
    for line in id_map['location']:
        if min_location is None:
            min_location = line["id_start"]
        else:
            min_location = min(min_location, line["id_start"])
    summary = min_location
    print(f"Part2 answer: {summary}")
    return summary

    # endregion part2

if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    main(infile)
