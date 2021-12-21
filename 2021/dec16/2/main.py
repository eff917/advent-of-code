from copy import deepcopy
from collections import Counter
url = '2021/dec16/input.txt'

with open(url, 'r') as infile:
    hex_message = infile.readline().strip()


# hex_message = 'C200B40A82'                  # 3         1+2
# hex_message = '04005AC33890'                # 54        6*9
# hex_message = '880086C3E88112'              # 7         min(7, 8, 9)
# hex_message = 'CE00C43D881120'              # 9         max(7,8,9)
# hex_message = 'D8005AC2A8F0'                # 1         5 < 15
# hex_message = 'F600BC2D8F'                  # 0         5 > 15
# hex_message = '9C005AC2F8F0'                # 0         5 == 15
# hex_message = '9C0141080250320F1802104A08'  # 1         1+3 == 2*2


message_length = len(hex_message)
hex_number  = int(hex_message, 16)
binary = f'{hex_number:0>{message_length*4}b}'

version_sum = 0
total_value = 0

# parse packet version and type
def parse_headers(message):
    packet_version = int(message[0:3],2)
    packet_type = int(message[3:6],2)
    packet = message[6:]
    print(f"Version: {packet_version}, type: {packet_type}")
    global version_sum
    version_sum += packet_version
    return (packet_version, packet_type, packet)

def parse_literal_block(binary_string):
    marker = binary_string[0]
    block = binary_string[1:5]
    binary_string = binary_string[5:]
    value = block
    # print(marker, value, binary_string)
    while marker == '1':
        marker = binary_string[0]
        block = binary_string[1:5]
        binary_string = binary_string[5:]
        value += block
        # print(value)
    return (int(value, 2), binary_string)


def parse_operator_package(message, operator_type):
    length_type = message[0]
    subvalues = []
    if length_type == '0':
        total_length = int(message[1:16], 2)
        message = message[16:]
        submessage = message[:total_length]
        message = message[total_length:]
        print(f"Submessage: {submessage}")
        print(f"Operator packet type: {length_type}.")
        print(f"Operator packet length: {total_length}.")
        # parse subpackets
        while len(submessage) > 0:
            version, packet_type, submessage = parse_headers(submessage)
            # print(f"Version: {version}, type: {packet_type}")
            if packet_type == 4:
                subvalue, submessage = parse_literal_block(submessage)
                print(f"Literal packet found with value: {subvalue}")
                subvalues.append(subvalue)
            else:
                print(f"Operator packet found.")
                submessage, subvalue = parse_operator_package(submessage, packet_type)
                subvalues.append(subvalue)
    else:
        # this is the subpacket count instead of the length
        subpacket_count = int(message[1:12], 2)
        message = message[12:]
        print(f"Operator packet type: {length_type}.")
        print(f"Operator packet count: {subpacket_count}.")
        for i in range(subpacket_count):
            version, packet_type, message = parse_headers(message)
            if packet_type == 4:
                subvalue, message = parse_literal_block(message)
                subvalues.append(subvalue)
            else:
                if packet_type == 0:
                    print(f"Sum operator packet")
                    # their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet
                elif packet_type == 1:
                    print(f"Product operator packet")
                    # their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
                elif packet_type == 2:
                    print(f"Minimum operator packet")
                    # their value is the minimum of the values of their sub-packets
                elif packet_type == 3:
                    print(f"Maximum operator packet")
                    # their value is the maximum of the values of their sub-packets
                elif packet_type == 5:
                    print(f"Greather than operator packet")
                    # their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets
                elif packet_type == 6:
                    print(f"Less than operator packet")
                    # their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets
                elif packet_type == 7:
                    print(f"Equal to operator packet")
                    # their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets
                message, subvalue = parse_operator_package(message, packet_type)
                subvalues.append(subvalue)
    print(f"Rest of the message: {message}")
    print(subvalues, operator_type)
    # SUM
    if operator_type == 0:
        value = 0
        for elem in subvalues:
            value += elem
    # PRODUCT
    elif operator_type == 1:
        value = 1
        for elem in subvalues:
            value *= elem
    elif operator_type == 2:
        value = min(subvalues)
    elif operator_type == 3:
        value = max(subvalues)
    elif operator_type == 5:
        if subvalues[0] > subvalues[1]:
            value = 1
        else:
            value = 0
    elif operator_type == 6:
        if subvalues[0] < subvalues[1]:
            value = 1
        else:
            value = 0
    elif operator_type == 7:
        if subvalues[0] == subvalues[1]:
            value = 1
        else:
            value = 0
    return message, value

message = binary

while '1' in message:
    version, packet_type, message = parse_headers(binary)
    if packet_type == 4:
        print("Literal packet found")
        value, message = parse_literal_block(message)
        print(f"Value of the literal packet: {value}")
        # TODO: read by five bits, of which the MSB is only masking if it's the last packet.
    else:
        print("Operator packet found")
        print(f"Message before parsing operator packet: {message}")
        if packet_type == 0:
            print(f"Sum operator packet")
            # their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet
        elif packet_type == 1:
            print(f"Product operator packet")
            # their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        elif packet_type == 2:
            print(f"Minimum operator packet")
            # their value is the minimum of the values of their sub-packets
        elif packet_type == 3:
            print(f"Maximum operator packet")
            # their value is the maximum of the values of their sub-packets
        elif packet_type == 5:
            print(f"Greather than operator packet")
            # their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets
        elif packet_type == 6:
            print(f"Less than operator packet")
            # their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets
        elif packet_type == 7:
            print(f"Equal to operator packet")
            # their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets

        message, value = parse_operator_package(message, packet_type)
        print(f"Rest of the message after parsing operator packet: {message}")
        print(value)

print(f"Total version sum: {version_sum}")