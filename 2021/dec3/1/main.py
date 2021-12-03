bits = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        bits.append(line.strip())


linecount = len(bits)
MSB = []
LSB = []
for i in range(len(bits[0])):
    bitsum = 0
    for code in bits:
        bitsum += int(code[i])
    if bitsum*2 > linecount:
        MSB.append('1')
        LSB.append('0')
    else:
        MSB.append('0')
        LSB.append('1')

gamma = (int(''.join(MSB), 2))
epsilon = (int(''.join(LSB), 2))

print(gamma * epsilon)
