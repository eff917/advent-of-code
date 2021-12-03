adapters = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        adapters.append(int(line.strip()))

# add socket
adapters.append(0)
# add device
adapters.append(max(adapters) + 3)
# sort adapters
adapters.sort()

def valid_configuration(adapter_list):
    differences = {}
    prev = 0
    for rating in adapter_list:
        difference = rating - prev
        if difference in differences.keys():
            differences[difference] +=1
        else:
            differences[difference] = 1
        prev = rating
    # The configuration is invalid, if there is a difference of 4 or higher
    if max(differences.keys()) > 3:
        return False
    else:
        return True

valid_conf_count = 0

if valid_configuration(adapters):
    valid_conf_count += 1

print(valid_conf_count)

# number of adapters to remove from list
for i in range(len(adapters)):
    pass
