from copy import copy


class Monkey:
    def __init__(self):
        self.items = []
        self.operator = None
        self.operand = None
        self.test_divisor = None
        self.true_throw = -1
        self.false_throw = -1
        self.num_inspections = 0

    def __str__(self):
        return f'Monkey N: {self.items}'

    def inspect_items(self):
        throws = []
        for i, item in enumerate(self.items):
            if self.operator == '+':
                new_val = item + self.operand
            elif self.operator == '*':
                new_val = item * self.operand
            elif self.operator == '**':
                new_val = item**self.operand
            else:
                raise ValueError(f'Unknown operator {self.operator}')

            new_val //= 3

            if new_val % self.test_divisor == 0:
                throws.append(self.true_throw)
            else:
                throws.append(self.false_throw)

            self.items[i] = new_val
            self.num_inspections += 1

        return throws


def build_monkeys(lines):
    monkeys = []
    for line in lines:
        if not line:
            continue
        elif line.startswith('Monkey'):
            monkey = Monkey()
        elif line.startswith('Starting items'):
            items = line.split(': ')[1]
            list_of_items = [int(item) for item in items.split(',')]
            monkey.items = list_of_items
        elif line.startswith('Operation'):
            operation_tokens = line.split()
            monkey.operator = operation_tokens[-2]
            operand = operation_tokens[-1]
            if operand == 'old':
                monkey.operator = '**'
                monkey.operand = 2
            else:
                monkey.operand = int(operand)
        elif line.startswith('Test'):
            monkey.test_divisor = int(line.split()[-1])
        elif line.startswith('If true'):
            monkey.true_throw = int(line.split()[-1])
        elif line.startswith('If false'):
            monkey.false_throw = int(line.split()[-1])
            monkeys.append(monkey)
    return monkeys


def run_round(monkeys):
    for monkey in monkeys:
        throws = monkey.inspect_items()
        for throw in throws:
            monkeys[throw].items.append(monkey.items.pop(0))


def main(lines):
    monkeys = build_monkeys(lines)
    for _ in range(20):
        run_round(monkeys)
    sorted_monkeys = sorted(monkeys, key=lambda m: m.num_inspections, reverse=True)
    return sorted_monkeys[0].num_inspections * sorted_monkeys[1].num_inspections


if __name__ == '__main__':
    with open('../../data/2022/input11.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
