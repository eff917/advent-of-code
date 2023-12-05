code = []
accumulator = 0
executed_lines = set()

with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        codeline = line.strip().split(' ')
        code.append([codeline[0], int(codeline[1])])

current_line = 0
while current_line not in executed_lines:
    # print(executed_lines)
    # print(accumulator)
    # print(current_line)
    # print(code[current_line])
    executed_lines.add(current_line)
    if code[current_line][0] == 'acc':
        accumulator += code[current_line][1]
        current_line += 1
    if code[current_line][0] == 'jmp':
        current_line += code[current_line][1]
    if code[current_line][0] == 'nop':
        current_line += 1

# print(executed_lines)
print(accumulator)