mask = None
registers = {}
with open('2020/dec14/input.txt', 'r') as infile:
    for line in infile:
        line = line.strip().split(' = ')
        if line[0] == "mask":
            mask = line[1]
        else:
            address = bin(int(line[0][4:-1])).replace('0b', '').rjust(len(mask), '0')
            value = int(line[1])
            number_of_x = mask.count('X')
            # print(number_of_x)
            effective_addresses = ['']
            for i in range(len(mask)):
                for j in range(len(effective_addresses)):
                    # override to 1
                    if mask[i] == '1':
                        effective_addresses[j] += '1'
                    # keep original
                    elif mask[i] == '0':
                        effective_addresses[j] += address[i]
                    # create 2, one with 0, another with 1
                    else:
                        effective_addresses.append(effective_addresses[j] + '1')
                        effective_addresses[j] += '0'
            for address in effective_addresses:
                registers[int(address, 2)] = value


# print(mask)
# print(registers)
sum = 0
for number in registers.values():
    sum += number

print(sum)