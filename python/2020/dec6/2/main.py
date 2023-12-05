import string
sum = 0
answers = set(string.ascii_lowercase)
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        useranswers = set()
        line = line.strip()
        if len(line) == 0:
            sum += len(answers)
            answers = set(string.ascii_lowercase)
        else:
            for char in line:
                useranswers.add(char)
            answers = answers & useranswers

print(sum)
