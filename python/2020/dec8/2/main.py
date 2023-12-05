from os import truncate


code = []

with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        codeline = line.strip().split(' ')
        code.append([codeline[0], int(codeline[1])])



def run_code():
    accumulator = 0
    executed_lines = []
    current_line = 0
    while current_line not in executed_lines and current_line < len(code):
        executed_lines.append(current_line)
        if code[current_line][0] == 'acc':
            accumulator += code[current_line][1]
            current_line += 1
        elif code[current_line][0] == 'jmp':
            current_line += code[current_line][1]
        elif code[current_line][0] == 'nop':
            current_line += 1
    # print(executed_lines)
    if current_line in executed_lines:
        return False
    if current_line >= len(code):
        return accumulator
code_successful = False
# print(code)
run_code()
for idx, line in enumerate(code):
    if line[0] == 'jmp':
        # print(f'changing line {idx}')
        code[idx][0] = 'nop'
        # print(code)
        code_successful = run_code()
        if code_successful:
            print(code_successful)
            print(f"Changed line {idx} from jmp to nop")
            print(f"Accumulator value: {code_successful}")
            break
        else:
            code[idx][0] = 'jmp'
    if line[0] == 'nop':
        # print(f'changing line {idx}')
        code[idx][0] = 'jmp'
        # print(code)
        code_successful = run_code()
        if code_successful:
            print(code_successful)
            print(f"Changed line {idx} from nop to jmp")
            print(f"Accumulator value: {code_successful}")
            break
        else:
            code[idx][0] = 'nop'
    
                

