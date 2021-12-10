url = '2021/dec10/input.txt'
# url = '2021/dec10/input-example.txt'
# url = '2021/dec10/input-valid.txt'
# url = '2021/dec10/input-corrupted.txt'

max_length = 0
lines = []
with open(url, 'r') as infile:
    for line in infile:
        line = line.strip()
        lines.append(list(line))
        max_length = max(max_length, len(line))

def is_valid(codeline: list, openers: list):
    # print(f"{''.join(codeline):30} {''.join(openers):30}")
    if len(codeline) > 0:
        if codeline[0] in '[{<(':
            openers.append(codeline[0])
            codeline = codeline[1:]
            return is_valid(codeline, openers)
        else:
            if openers[-1] == '[' and codeline[0] == ']':
                codeline = codeline[1:]
                openers = openers[:-1]
                return is_valid(codeline, openers)
            elif openers[-1] == '{' and codeline[0] == '}':
                codeline = codeline[1:]
                openers = openers[:-1]
                return is_valid(codeline, openers)
            elif openers[-1] == '(' and codeline[0] == ')':
                codeline = codeline[1:]
                openers = openers[:-1]
                return is_valid(codeline, openers)
            elif openers[-1] == '<' and codeline[0] == '>':
                codeline = codeline[1:]
                openers = openers[:-1]
                return is_valid(codeline, openers)
            else:
                if codeline[0] == ')':
                    value = 3
                if codeline[0] == '}':
                    value = 1197
                if codeline[0] == ']':
                    value = 57
                if codeline[0] == '>':
                    value = 25137
                return(f'Corrupt char is {codeline[0]} worth {value} points.')

    else:
        if len(openers) > 0:
            print(f"Openers left: {''.join(openers)}")
            openers.reverse()
            value = 0
            for opener in openers:
                if opener == '(':
                    value = value*5 + 1
                elif opener == '[':
                    value = value*5 + 2
                elif opener == '{':
                    value = value*5 + 3
                elif opener == '<':
                    value = value*5 + 4
            print(f"Total value: {value}")
            return value
        else:
            return 'Valid'

totals = []
for line in lines:
    line_value = is_valid(line, [])
    if type(line_value) is int:
        print(line_value)
        totals.append(line_value)

totals = sorted(totals)
print(totals)
print(totals[len(totals)//2])