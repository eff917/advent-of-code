mask = None
registers = {}
with open('2020/dec14/input.txt', 'r') as infile:
    for line in infile:
        line = line.strip().split(' = ')
        if line[0] == "mask":
            mask = line[1]
        else:
            binary = bin(int(line[1])).replace('0b', '').rjust(len(mask), '0')
            effective = ''
            for i in range(len(mask)):
                if mask[i] == '1':
                    effective += '1'
                elif mask[i] == '0':
                    effective += '0'
                else:
                    effective += binary[i]

            registers[int(line[0][4:-1])] = effective
print(mask)
print(registers)
sum = 0
for number in registers.values():
    sum += int(number, 2)

print(sum)