import pprint

bagrules = {}

next_set = set()
with open('../input2.txt', 'r') as inputfile:
    for line in inputfile:
        # remove newline
        line = line.strip()
        # print(line)
        # hed becomes a bag type, tail becomes what it contains
        head, tail = line.split(' bags contain ')
        # create an empty dict for every bag type
        bagrules[head] = {}
        # split contain by spaces
        fields = tail.split(' ')
        bag_type = ""
        # print(head)
        if tail != 'no other bags.':
            # every rule is made of 4 fields: <quantity> <bag colormod> <bag color> [bags,|bags.|bag,|bag.]
            for i in range(len(fields)):
                if i%4 == 0:
                    bag_count=int(fields[i])
                if i%4 == 1:
                    bag_type = f"{fields[i]} "
                if i%4 == 2:
                    bag_type += fields[i]
                    # print(f"  {bag_count} {bag_type}")
                    bagrules[head][bag_type]=bag_count
        else:
            # print(f"  0 none")
            # If a bag contains no aother bags, set the rule value to None
            bagrules[head] = None

# print parsed rules
# pp.pprint(bagrules)

my_bags = {}
# for key in bagrules:
#     my_bags[key] = 0
my_bags['shiny gold'] = 1

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(my_bags)

prev_bags = {
    'shiny gold': 1
}
new_bags = {}

for bag, quantity in prev_bags.items():
    # if a bag containes other bags
    if bagrules[bag] is not None:
        # go through each rule for the bag
        for new_bag_name, new_bag_value in bagrules[bag].items():
            # add the new bags to new_bag multiplied by the quantity of bags we have
            new_bags[new_bag_name] = new_bag_value*quantity
# pp.pprint(new_bags)

# add the new bags to the total number of bags
for key, value in new_bags.items():
    if key not in my_bags.keys():
        my_bags[key] = value
    else:
        my_bags[key] += value

pp.pprint(my_bags)
cycle = 1
# repeat cycle until we have no new bags to add
while new_bags != {}:
    # rotate variables
    # in each cycle we want to add only the new bags contained inside the bags from in the previous cycle
    prev_bags = new_bags.copy()
    new_bags = {}

    # go through each bag type from the previous cycle
    for bag, quantity in prev_bags.items():
        # if the bag contains other bags
        if bagrules[bag] is not None:
            # go through the rules for the current bag
            for new_bag_name, new_bag_value in bagrules[bag].items():
                # add the new bag to the variable, multiplied by the current quantity of containing bag
                new_bags[new_bag_name] = new_bag_value*quantity
    # pp.pprint(new_bags)
    # add the new bags to the total number of bags
    for key, value in new_bags.items():
        if key not in my_bags.keys():
            my_bags[key] = value
        else:
            my_bags[key] += value
    # print(f"cycle: {cycle}")
    cycle += 1
    # print("My bags")
    pp.pprint(my_bags)
    # print("New bags added")
    # pp.pprint(new_bags)

# pp.pprint(my_bags)

sum = 0
for value in my_bags.values():
    # print(value)
    sum += value
# we dont count the shiny gold bag itself
print(sum - 1)
