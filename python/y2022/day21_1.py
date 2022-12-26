class Monkey:
    def __init__(self, mid, op, all_monkeys):
        self.monkey_id = mid
        self.all_monkeys = all_monkeys
        if len(op.split()) == 1:
            self.operation = lambda: int(op)
        else:
            param1, operator, param2 = op.split()
            if operator == '+':
                self.operation = (
                    lambda: self.all_monkeys[param1]() + self.all_monkeys[param2]()
                )
            elif operator == '-':
                self.operation = (
                    lambda: self.all_monkeys[param1]() - self.all_monkeys[param2]()
                )
            elif operator == '*':
                self.operation = (
                    lambda: self.all_monkeys[param1]() * self.all_monkeys[param2]()
                )
            elif operator == '/':
                self.operation = (
                    lambda: self.all_monkeys[param1]() / self.all_monkeys[param2]()
                )
            else:
                print('why are you here')

    def __call__(self, *args, **kwargs):
        return self.operation()


def build_monkeys(lines):
    monkeys = {}
    for line in lines:
        monkey_id, monkey_op = line.split(':')
        monkeys[monkey_id] = Monkey(monkey_id, monkey_op, monkeys)

    return monkeys


def main(lines):
    monkeys = build_monkeys(lines)
    return monkeys['root']()


if __name__ == '__main__':
    with open('../../data/2022/input21.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
