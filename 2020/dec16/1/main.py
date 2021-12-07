from copy import deepcopy
filename = '2020/dec16/input.txt'
# filename = '2020/dec16/input-example.txt'

fields = {}
other_tickets = []
ticket_fields = []
with open(filename, 'r') as infile:
    line = infile.readline()
    while line.strip() != '':
        line = line.strip()
        fieldid, fieldvalues = line.split(': ')
        fieldranges = fieldvalues.split(' or ')
        for i in range(len(fieldranges)):
            fieldranges[i] = fieldranges[i].split('-')
            fieldranges[i] = [int(x) for x in fieldranges[i]]
        fields[fieldid] = fieldranges
        line = infile.readline()
    if infile.readline().strip() == 'your ticket:':
        my_ticket = infile.readline().strip().split(',')
        my_ticket = [int(x) for x in my_ticket]
        for i in range(len(my_ticket)):
            ticket_fields.append([])
    infile.readline()
    infile.readline()
    line = infile.readline().strip()
    while line:
        ticket = [int(x) for x in line.split(',')]
        for i, ticketfield in enumerate(ticket):
            ticket_fields[i].append(ticketfield)
        other_tickets.append(ticket)
        line = infile.readline().strip()

def is_valid_field(fieldvalue):
    for field in fields.values():
        for range in field:
            if fieldvalue <= range[1] and fieldvalue >= range[0]:
                print(f"{fieldvalue} is valid for range {range}")
                return True
    print(f"{fieldvalue} did not match any ranges")
    return False

fieldcount = len(fields)
invalid_sum = 0
print(fields)
print(my_ticket)
print(other_tickets)

valid_tickets = deepcopy(other_tickets)

for ticked_id, ticket in enumerate(valid_tickets):
    for field in ticket:
        if not is_valid_field(field):
            invalid_sum += field
            del valid_tickets[ticked_id]

# print(valid_tickets)
filed_id_name = {}
for field_id, field in enumerate(ticket_fields):
    print(f"{field_id} {field}")
print(invalid_sum)