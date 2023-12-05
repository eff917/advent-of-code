
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
        sum_to_find = numbers[preamble_size + i]
        print(sum_to_find)
        break

print("starting phase2")
for i in range(len(numbers)):
    tempsum = 0
    list_of_numbers = []
    j = i
    while tempsum < sum_to_find:
        tempsum += numbers[j]
        
        j += 1
    if tempsum == sum_to_find:
        print(f"starting index of block: {i}")
        print(f"ending index of block: {j}")
        print(f"list of numbers: {numbers[i:j]}")
        tempsum = 0
        for idx in range(i,j):
            tempsum += numbers[idx]
        print(tempsum)
        print(f"smallest number: {min(numbers[i:j])}")
        print(f"largest number: {max(numbers[i:j])}")
        print(f"sum of smallest and largest: {min(numbers[i:j]) + max(numbers[i:j])}")
        break
