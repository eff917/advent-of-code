file = '2020/dec16/input.txt'
# file = '2020/dec16/input-example.txt'

field_rules = {}
all_tickets = []
with open(file, 'r') as infile:
    line = infile.readline().strip()
    while line != '':
        field_name, field_ranges = line.split(': ')
        field_ranges = field_ranges.split(' or ')
        for i, range in enumerate(field_ranges):
            field_ranges[i] = range.split('-')
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

# check number against field rule
def is_valid_field(field, ranges):
    for range in ranges:
        if field >= range[0] and field <= range[1]:
            return True
    return False
print(len(all_tickets))
valid_tickets = []
for ticket_id, ticket in enumerate(all_tickets):
    ticket_is_valid = True
    for field_rule_ranges in field_rules.values():
        for field in ticket:
            if not is_valid_field(field, field_rule_ranges):
                ticket_is_valid = False
    if ticket_is_valid:
        valid_tickets.append(ticket)
print(len(valid_tickets))
