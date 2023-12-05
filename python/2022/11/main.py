from collections import namedtuple
import os
from copy import deepcopy
import typing
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

Inspect_function = namedtuple('Inspect_function', ['operator', 'value'])

class Monkey:
    def __init__(self, id: int, inventory: typing.List, pass_id: int, fail_id: int, test_divisor: int, inspect_function: Inspect_function ) -> None:
        self.inspect_count = 0
        self.id = id
        self.inventory = inventory
        self.pass_id = pass_id
        self.fail_id = fail_id
        self.test_divisor = test_divisor
        self.inspect_function = inspect_function

    def __repr__(self) -> str:
        return f"Id: {self.id}, inv: {self.inventory}, insp: {self.inspect_function}, test: divisibe by {self.test_divisor}, pass: {self.pass_id}, fail: {self.fail_id}, Inspect count: {self.inspect_count}\n"

    def receive(self, item: int) -> None:
        self.inventory.append(item)
    
    def test(self, item) -> tuple[int, int]:
        # remove item from inventory
        if item % int(self.test_divisor) == 0:
            return self.pass_id
        else:
            return self.fail_id
    
    def inspect(self, item):
        self.inspect_count += 1
        if self.inspect_function.value == 'old':
            value = item
        else:
            value = int(self.inspect_function.value)
    
        if self.inspect_function.operator == '+':
            return item + value
        elif self.inspect_function.operator == '*':
            return item * value
    def get_item(self):
        try:
            return self.inventory.pop(0)
        except IndexError:
            return None




def solution(infile):
    monkeys = {}
    for line in infile:
        line = line.strip().split()
        if len(line) > 0:
            if line[0] == "Monkey":
                monkey_id = int(line[1][0:-1])
            elif line[0] == "Starting":
                items = []
                for item in line[2:]:
                    items.append(int(item.replace(',','')))

            elif line[0] == "Operation:":
                inspect_function = Inspect_function(operator=line[4], value=line[5])
            elif line[0] == "Test:":
                test_divisor = int(line[3])
            elif line[0] == "If":
                if line[1] == "true:":
                    pass_id = int(line[5])
                else:
                    fail_id = int(line[5])
        else:
            monkeys[monkey_id] = Monkey(id=monkey_id, inventory=items, pass_id=pass_id, fail_id=fail_id, inspect_function=inspect_function, test_divisor=test_divisor)
    monkeys[monkey_id] = Monkey(id=monkey_id, inventory=items, pass_id=pass_id, fail_id=fail_id, inspect_function=inspect_function, test_divisor=test_divisor)

    # print(monkeys)

    for i in range(20):
        # print("round {i+1}")
        for monkey_id, monkey in monkeys.items():
            item = monkey.get_item()
            while item is not None:
                # print(f"Testing {item}")
                item = monkey.inspect(item)
                # print(f"Inspecting {item}")
                item = item // 3
                # print(f"Testing {item}")
                target = monkey.test(item)
                # print(f"Item with worry level {item} is thrown to {target}")
                monkeys[target].receive(item)
                item = monkey.get_item()
        # print(monkeys)
    inspect_counts = []
    for monkey in monkeys.values():
        inspect_counts.append(monkey.inspect_count)
    inspect_counts.sort()
    print(inspect_counts)
    print(f"Part1: {inspect_counts[-1]*inspect_counts[-2]}")

print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

# print("Real")
# with open(infile, 'r') as infile:
#     solution(infile)
