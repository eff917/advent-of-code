file = '2020/dec16/input.txt'
# file = '2020/dec16/input-example.txt'

field_rules = {}
all_tickets = []
with open(file, 'r') as infile:
    line = infile.readline().strip()
    while line != '':
        field_name, field_ranges = line.split(': ')
        field_ranges = field_ranges.split(' or ')
        for i, mrange in enumerate(field_ranges):
            field_ranges[i] = mrange.split('-')
            field_ranges[i] = [int(x) for x in field_ranges[i]]
        field_rules[field_name] = field_ranges
        line = infile.readline().strip()
    infile.readline()
    my_ticket = [int(x) for x in infile.readline().strip().split(',')]
    infile.readline()
    infile.readline()
    line = infile.readline().strip()
    while line:
        all_tickets.append([int(x) for x in line.split(',')])
        line = infile.readline().strip()
    

# print(field_rules)
# print(my_ticket)
# for ticket in all_tickets:
#     print(ticket)

# check number against all field rules
def is_valid_field(field):
    range_list = field_rules.values()
    for ranges in range_list:
        for mrange in ranges:
            if field >= mrange[0] and field <= mrange[1]:
                return True
    return False
print(f"All tickets: {len(all_tickets)}")
valid_tickets = []
for ticket_id, ticket in enumerate(all_tickets):
    ticket_is_valid = True
    for field in ticket:
        if not is_valid_field(field):
            ticket_is_valid = False
    if ticket_is_valid:
        valid_tickets.append(ticket)
print(f"Valid tickets: {len(valid_tickets)}")

# create a list all the values for each field, to test them against field_rules

all_fields = {}
for ticket in valid_tickets:
    for field_id, field_value in enumerate(ticket):
        try:
            all_fields[field_id].add(field_value)
        except KeyError:
            all_fields[field_id] = {field_value}

def field_passes_rule(field_set, rule_ranges):
    valid_fields = set()
    for field in field_set:
        for rule in rule_ranges:
            if field >= rule[0] and field <= rule[1]:
                valid_fields.add(field)
    # if all fields are valid:
    if valid_fields == field_set:
        return True
    else:
        return False
                
        
field_id_possible_names = {}
# iterate over each field
for field_id, field_value in all_fields.items():
    # print(f"{field_id}: {sorted(field_value)}")
    # iterate over each field rule
    for name, ranges in field_rules.items():
        if field_passes_rule(field_value, ranges):
            print(f"{field_id} passed check for {name}")
            try:
                field_id_possible_names[field_id].add(name)
            except KeyError:
                field_id_possible_names[field_id] = {name}
        else:
            print(f"{field_id} failed check for {name}")


for key, value in field_id_possible_names.items():
    print(f"{key}: {value}")

def remove_name_from_set(fieldname, namesdict):
    for key in namesdict.keys():
        if fieldname in namesdict[key] and len(namesdict[i]) > 1:
            namesdict[key].remove(fieldname)
    return namesdict

for i in range(15):
    for field_id in field_id_possible_names.keys():
        if len(field_id_possible_names[field_id]) == 1:
            for name in field_id_possible_names[field_id]:
                for field_id2 in field_id_possible_names:
                    if name in field_id_possible_names[field_id2] and len(field_id_possible_names[field_id2]) > 1:
                        field_id_possible_names[field_id2].remove(name)

print()
for key, value in field_id_possible_names.items():
    print(f"{key}: {value}")
print()
my_ticket_dict = {}

for id, value in enumerate(my_ticket):
    print(f"{field_id_possible_names[id]}: {value}")
    for fieldname in field_id_possible_names[id]:
        my_ticket_dict[fieldname] = value

sum = 1
for key, value in my_ticket_dict.items():
    if 'departure' in key:
        sum *= value

print(sum)
