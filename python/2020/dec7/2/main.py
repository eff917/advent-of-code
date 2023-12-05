import pprint

bagrules = {}

next_set = set()
with open('../input.txt', 'r') as inputfile:
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

pp = pprint.PrettyPrinter(indent=2)
# print parsed rules
# pp.pprint(bagrules)
# for key, value in bagrules.items():
#     print(f"{key}: {value}")

my_bags = {}

prev_bags = {
    'shiny gold': 1
}
# this can be anything, just need to be not and empty list to start the cycle
new_bags = 'start'

def get_contained_bags(current_bag_list):
    new_bag_list = {}
    for bag_type, quantity in current_bag_list.items():
        if bagrules[bag_type] is not None:
            for new_bag_type, new_bag_quanty in bagrules[bag_type].items():
                if new_bag_type in new_bag_list.keys():
                    new_bag_list[new_bag_type] += quantity*new_bag_quanty
                else:
                    new_bag_list[new_bag_type] = quantity*new_bag_quanty
    return new_bag_list

while new_bags != {}:
    # get new bags
    new_bags = get_contained_bags(prev_bags)
    # add new bags to all bags
    for bag, value in new_bags.items():
        if bag not in my_bags.keys():
            my_bags[bag] = value
        else:
            my_bags[bag] += value
    # move new bags into old for next cycle
    prev_bags = new_bags.copy()

sum = 0
for bag, count in my_bags.items():
    sum += count
print(my_bags)
print(sum)