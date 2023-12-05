import os
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    count1 = 0
    count2 = 0
    for line in infile:
        line  = line.strip()
        first, second = line.split(',')
        first_start, first_end = first.split('-')
        second_start, second_end = second.split('-')
        first_start, first_end, second_start, second_end = int(first_start), int(first_end), int(second_start), int(second_end)
        first_zone = set(range(first_start, first_end+1))
        second_zone = set(range(second_start, second_end+1))
        # print(first_zone, second_zone)

        if first_zone.union(second_zone) == first_zone or first_zone.union(second_zone) == second_zone:
            count1 += 1
        if len(first_zone.union(second_zone)) < len(first_zone) + len(second_zone):
            count2 += 1
    print(f"Number of fully contined pairs (part1): {count1}")
    print(f"Overlapping zones (part2): {count2}")

print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)
print("Real")
with open(infile, 'r') as infile:
    solution(infile)

