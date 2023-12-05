
numbers = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        line = int(line.strip())
        numbers.append(line)


preamble_size = 25

def is_valid(number, preamble_list):
    # print(f"Checking {number} in {preamble_list}")
    set_of_sums = set()
    # remove duplicate entries
    unique_preable_list = list(set(preamble_list))
    # create a set of sums
    for a in unique_preable_list:
        for b in unique_preable_list:
            if a != b:
                set_of_sums.add(a+b)
    if number in set_of_sums:
        return True
    else:
        return False


for i in range(len(numbers) - preamble_size):
    if not is_valid(numbers[preamble_size+i], numbers[i:i+preamble_size]):
        print(numbers[preamble_size + i])
        break
