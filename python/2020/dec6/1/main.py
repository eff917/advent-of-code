sum = 0
answers = set()
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        line = line.strip()
        if len(line) == 0:
            sum += len(answers)
            answers = set()
        else:
            for char in line:
                answers.add(char)

print(sum)
