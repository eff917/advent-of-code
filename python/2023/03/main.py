import os

# region part1
part = "part1"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"

summary = 0
numbers = []
symbols = []
with open(infile) as infile:
    y=0
    for line in infile:
        # reset x and number
        x=0
        number = ""
        for char in line.strip() + ".":
            # found a digit
            if char.isdigit():
                # start of a number, store start coords
                if number == "":
                    start_x = x
                    start_y = y
                # add chacter to number
                number += char
                # faulty check, just added a dot to the end of each line
                # # last character in line
                # if x == len(line):
                #     numbers.append({"value": int(number), "start_x": start_x, "start_y": start_y, "end_x": x, "end_y": y})
                #     number = ''
            elif char == '.':
                # end of a number
                if number != '':
                    # record number with value and coords
                    numbers.append({"value": int(number), "start_x": start_x, "start_y": start_y, "end_x": x-1, "end_y": y})
                    number = ''
            # we found a part
            else:
                symbols.append((x,y))
                if number != '':
                    # record number with value and coords
                    numbers.append({"value": int(number), "start_x": start_x, "start_y": start_y, "end_x": x-1, "end_y": y})
                    number = ''

            x+=1
        y+=1

for number in numbers:
    # print(number)
    is_partnumber = False
    for y in range(number["start_y"]-1, number["end_y"]+2):
        for x in range(number["start_x"]-1, number["end_x"]+2):
            # print(f"checking {x} {y}")
            if (x, y) in symbols:
                is_partnumber = True
    if is_partnumber:
        summary += number["value"]
        # print(f"{number["value"]} is a partnumber")

# print(symbols)
print(f"Part1 answer: {summary}")
                    
# endregion part1

# region part2
part = "part2"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"

summary = 0
numbers = []
symbols = []
with open(infile) as infile:
    y=0
    for line in infile:
        # reset x and number
        x=0
        number = ""
        for char in line.strip() + ".":
            # found a digit
            if char.isdigit():
                # start of a number, store start coords
                if number == "":
                    start_x = x
                    start_y = y
                # add chacter to number
                number += char
                # faulty check, just added a dot to the end of each line
                # # last character in line
                # if x == len(line):
                #     numbers.append({"value": int(number), "start_x": start_x, "start_y": start_y, "end_x": x, "end_y": y})
                #     number = ''
            elif char == '.':
                # end of a number
                if number != '':
                    # record number with value and coords
                    numbers.append({"value": int(number), "start_x": start_x, "start_y": start_y, "end_x": x-1, "end_y": y})
                    number = ''
            # we found a gear
            elif char == '*':
                symbols.append((x,y))
                if number != '':
                    # record number with value and coords
                    numbers.append({"value": int(number), "start_x": start_x, "start_y": start_y, "end_x": x-1, "end_y": y})
                    number = ''

            x+=1
        y+=1

gear_numbers = {}
for number in numbers:
    # print(number)
    for y in range(number["start_y"]-1, number["end_y"]+2):
        for x in range(number["start_x"]-1, number["end_x"]+2):
            # print(f"checking {x} {y}")
            if (x, y) in symbols:
                if f"{x} {y}" in gear_numbers.keys():
                    gear_numbers[f"{x} {y}"].append(number["value"])
                else:
                    gear_numbers[f"{x} {y}"]=[number["value"],]
    
# print(gear_numbers)
for gear in gear_numbers.values():
    if len(gear) == 2:
        summary += gear[0]*gear[1]
# print(symbols)
print(f"Part2 answer: {summary}")
# endregion part2
