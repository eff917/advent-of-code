bits = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        bits.append(line.strip())



def select_lines_and_reduce(bitlist, full_bitlist, isMSB):
    linecount = len(bitlist)
    sum = 0
    reduced_list = []
    full_list = []
    for codeline in bitlist:
        sum += int(codeline[0])
    # MSB is one
    if sum * 2 >= linecount:
        if isMSB:
            MSB = '1'
        else:
            MSB = '0'
    else:
        if isMSB:
            MSB = '0'
        else:
            MSB = '1'
    for idx, codeline in enumerate(bitlist):
        if codeline[0] == MSB:
            # remove line
            reduced_list.append(bitlist[idx][1:])
            full_list.append(full_bitlist[idx])

    return reduced_list, full_list

# print(f"{len(bits)} {len(bits[0])}")
o2_full_bits = bits.copy()
o2_bits = bits.copy()
while len(o2_bits) > 1:
    o2_bits, o2_full_bits = select_lines_and_reduce(o2_bits, o2_full_bits, True)
    # print(bits[0])
    # print(f"{len(bits)} {len(bits[0])}")

O2rating = int(o2_full_bits[0], 2)
print(f"O2 generator rating: {O2rating}")

co2_full_bits = bits.copy()
co2_bits = bits.copy()
while len(co2_bits) > 1:
    co2_bits, co2_full_bits = select_lines_and_reduce(co2_bits, co2_full_bits, False)
    # print(bits[0])
    # print(f"{len(bits)} {len(bits[0])}")

CO2rating = int(co2_full_bits[0], 2)
print(f"CO2 scrubber rating: {CO2rating}")

print(f"Life support rating: {O2rating*CO2rating}")