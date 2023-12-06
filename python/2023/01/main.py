import os
part = "part1"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"

with open(infile) as infile:
    summary = 0
    for line in infile:
        first_number = None
        last_number = None
        for char in line:
            if char.isdigit():
                last_number = char
                if first_number is None:
                    first_number = char

        line_number = int(first_number + last_number)
        # print(line)
        # print(line_number)
        summary += line_number

print(summary)

part = "part2"

infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"

with open(infile) as infile:
    summary = 0
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in infile:
        line_numbers = ""
        for i in range(len(line)):
            if line[i].isdigit():
                line_numbers += line[i]
                # jump to nect char in string
                continue
            for index, digit in enumerate(digits):
                if line[i:].startswith(digit):
                    line_numbers += str(index)
                    continue
        # print(line, line_numbers)
        summary += int(line_numbers[0] + line_numbers[-1])
print(summary)
