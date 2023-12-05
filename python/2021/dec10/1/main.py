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

# print(max_length)

def is_complete(codeline: list):
    openers = 0
    closers = 0
    for character in codeline:
        if character in '[{<(':
            openers += 1
        else:
            closers += 1
    print(f"Openers: {openers}, closers: {closers}")
    if openers == closers:
        return True
    else:
        return False

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
                print(f'Corrupt char is {codeline[0]} worth {value} points.')
                return value

    else:
        if len(openers) > 0:
            return "Incomplete"
        else:
            return 'Valid'

total = 0
for line in lines:
    # complete = is_complete(line)
    # print(f'The line is complete: {complete}')
    line_value = is_valid(line, [])
    if type(line_value) is int:
        total += line_value
        print(f"Total points so far: {total}")
    else:
        print(line_value)