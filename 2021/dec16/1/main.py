from copy import deepcopy
from collections import Counter
url = '2021/dec16/input.txt'
# url = '2021/dec16/input-example-2.txt'

with open(url, 'r') as infile:
    hex_message = infile.readline().strip()


# hex_message = '38006F45291200'
# hex_message = 'EE00D40C823060'

# hex_message = '8A004A801A8002F478' # version_sum: 16 good
# hex_message = '620080001611562C8802118E34' # version_sum: 12 good
# hex_message = 'C0015000016115A2E0802F182340' # version_sum: 23 good
# hex_message = 'A0016C880162017C3686B18A3D4780' # version_sim: 31 good


message_length = len(hex_message)
hex_number  = int(f"0x{hex_message}", 16)
binary = f'{hex_number:0>{message_length*4}b}'

version_sum = 0

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


def parse_operator_package(message):
    length_type = message[0]
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
                value, submessage = parse_literal_block(submessage)
                print(f"Literal packet found with value: {value}")
            else:
                print(f"Operator packet found.")
                submessage = parse_operator_package(submessage)
    else:
        # this is the subpacket count instead of the length
        subpacket_count = int(message[1:12], 2)
        message = message[12:]
        print(f"Operator packet type: {length_type}.")
        print(f"Operator packet count: {subpacket_count}.")
        for i in range(subpacket_count):
            version, packet_type, message = parse_headers(message)
            if packet_type == 4:
                value, message = parse_literal_block(message)
            else:
                message = parse_operator_package(message)
    print(f"Rest of the message: {message}")
    return message

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
        message = parse_operator_package(message)
        print(f"Rest of the message after parsing operator packet: {message}")

print(version_sum)