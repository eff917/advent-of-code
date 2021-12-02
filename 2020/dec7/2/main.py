import pprint

bagrules = {}

next_set = set()
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        line = line.strip()
        # print(line)
        head, tail = line.split(' bags contain ')
        bagrules[head] = {}
        fields = tail.split(' ')
        bag_type = ""
        # print(head)
        if tail != 'no other bags.':
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
            bagrules[head] = None

my_bags = {}
for key in bagrules:
    my_bags[key] = 0
my_bags['shiny gold'] = 1

pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(my_bags)

prev_bags = {
    'shiny gold': 1
}
new_bags = {}

for bag, quantity in prev_bags.items():
    if bagrules[bag] is not None:
        for new_bag_name, new_bag_value in bagrules[bag].items():
            new_bags[new_bag_name] = new_bag_value*quantity
# pp.pprint(new_bags)
for key, value in new_bags.items():
    my_bags[key] += value

cycle = 1
while new_bags != {}:
    prev_bags = new_bags.copy()
    new_bags = {}
    for bag, quantity in prev_bags.items():
        if bagrules[bag] is not None:
            for new_bag_name, new_bag_value in bagrules[bag].items():
                new_bags[new_bag_name] = new_bag_value*quantity
    # pp.pprint(new_bags)
    for key, value in new_bags.items():
        my_bags[key] += value
    print(f"cycle: {cycle}")
    cycle += 1
    print("My bags")
    pp.pprint(my_bags)
    print("New bags added")
    pp.pprint(new_bags)

sum = 0
for value in my_bags.values():
    # print(value)
    sum += value
print(sum)
