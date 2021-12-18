class SnailfishNumber:
    def __init__(self, pair, parent=None):
        self.nodes = {} if parent is None else parent.nodes
        self.parent = parent

        left, right = pair
        self.left = left if isinstance(left, int) else SnailfishNumber(left, self)
        self.node_val = 0 if not self.nodes else max(list(self.nodes.keys())) + 1
        self.nodes[self.node_val] = self
        self.right = right if isinstance(right, int) else SnailfishNumber(right, self)

    def renumber_nodes(self):
        self.nodes = {}
        self._renumber_nodes()

    def _renumber_nodes(self):
        if isinstance(self.left, SnailfishNumber):
            self.left._renumber_nodes()
        self.node_val = 0 if not self.nodes else max(list(self.nodes.keys())) + 1
        self.nodes[self.node_val] = self
        if isinstance(self.right, SnailfishNumber):
            self.right._renumber_nodes()

    def __str__(self):
        return str(self.raw_form())

    def __add__(self, other):
        return SnailfishNumber([self.raw_form(), other.raw_form()])

    @property
    def depth(self):
        return 1 if self.parent is None else self.parent.depth + 1

    def magnitude(self):
        left_val = self.left if isinstance(self.left, int) else self.left.magnitude()
        right_val = self.right if isinstance(self.right, int) else self.right.magnitude()
        return 3 * left_val + 2 * right_val

    def can_explode(self):
        return (
            (
                self.depth >= 5
                and isinstance(self.left, int)
                and isinstance(self.right, int)
            )
            or (isinstance(self.left, SnailfishNumber) and self.left.can_explode())
            or (isinstance(self.right, SnailfishNumber) and self.right.can_explode())
        )

    def can_split(self):
        return (
            (isinstance(self.left, int) and self.left >= 10)
            or (isinstance(self.right, int) and self.right >= 10)
            or (isinstance(self.left, SnailfishNumber) and self.left.can_split())
            or (isinstance(self.right, SnailfishNumber) and self.right.can_split())
        )

    def get_exploding_pair(self):
        if (
            self.depth >= 4
            and isinstance(self.left, int)
            and isinstance(self.right, int)
        ):
            return self

        if isinstance(self.left, SnailfishNumber):
            exploder = self.left.get_exploding_pair()
            if exploder:
                return exploder

        if isinstance(self.right, SnailfishNumber):
            return self.right.get_exploding_pair()

    def explode(self):
        if (
            self.depth >= 5
            and isinstance(self.left, int)
            and isinstance(self.right, int)
        ):
            self._explode()
            return True

        if isinstance(self.left, SnailfishNumber) and self.left.explode():
            return True

        if isinstance(self.right, SnailfishNumber):
            return self.right.explode()

    def _add_to_first_regular_number_to_left(self, value, node_val):
        if isinstance(self.right, int) and self.node_val < node_val:
            self.right += value
            return True
        if self.right._add_to_first_regular_number_to_left(value, node_val):
            return True
        if self.parent and self.parent._add_to_first_regular_number_to_left(value):
            return True
        if isinstance(self.left, int) and self.node_val < node_val:
            self.left += value
            return True
        return self.left._add_to_first_regular_number_to_left(value)

    def _add_to_first_regular_number_to_right(self, value):
        if isinstance(self.left, int):
            self.left += value
            return True
        if self.left._add_to_first_regular_number_to_left(value):
            return True
        if self.parent and self.parent._add_to_first_regular_number_to_right(value):
            return True
        if isinstance(self.right, int):
            self.right += value
            return True
        return self.right._add_to_first_regular_number_to_right(value)

    def _explode(self):
        leaves_to_left = sorted(
            [v for v in self.nodes.values() if v.node_val < self.node_val],
            key=lambda node: node.node_val,
            reverse=True,
        )

        for leaf in leaves_to_left:
            if isinstance(leaf.right, int):
                leaf.right += self.left
                break
            elif isinstance(leaf.left, int):
                leaf.left += self.left
                break

        leaves_to_right = sorted(
            [v for v in self.nodes.values() if v.node_val > self.node_val],
            key=lambda node: node.node_val,
        )
        for leaf in leaves_to_right:
            if isinstance(leaf.left, int):
                leaf.left += self.right
                break
            elif isinstance(leaf.right, int):
                leaf.right += self.right
                break

        if self.parent.left is self:
            self.parent.left = 0
        elif self.parent.right is self:
            self.parent.right = 0
        else:
            raise Exception('Did not expect to be here')

        del self.nodes[self.node_val]

    def raw_form(self):
        raw_left = self.left if isinstance(self.left, int) else self.left.raw_form()
        raw_right = self.right if isinstance(self.right, int) else self.right.raw_form()
        return [raw_left, raw_right]

    def _split_left(self):
        new_left = self.left // 2
        new_right = self.left // 2 + self.left % 2

        self.left = SnailfishNumber([new_left, new_right], self)

    def _split_right(self):
        new_left = self.right // 2
        new_right = self.right // 2 + self.right % 2

        self.right = SnailfishNumber([new_left, new_right], self)

    def split(self):
        answer = self._split()
        self._renumber_nodes()
        return answer

    def _split(self):
        if isinstance(self.left, int):
            if self.left >= 10:
                self._split_left()
                return True
        else:
            left_split = self.left.split()
            if left_split:
                return True

        if isinstance(self.right, int):
            if self.right >= 10:
                self._split_right()
                return True
        else:
            return self.right.split()

    def reduce(self):
        while True:
            if self.can_explode():
                self.explode()
                continue
            if self.can_split():
                self.split()
                continue
            break


def needs_to_explode(raw_snailfish_number):
    srep = str(raw_snailfish_number)
    depth = 0
    for c in srep:
        if depth == 5:
            return True
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1

    return False


def explode(raw_snailfish_number):
    sfn = SnailfishNumber(raw_snailfish_number)
    sfn.explode()
    return sfn.raw_form()


def split(raw_snailfish_number):
    sfn = SnailfishNumber(raw_snailfish_number)
    sfn.split()
    return sfn.raw_form()


def reduce(raw_snailfish_number):
    sfn = SnailfishNumber(raw_snailfish_number)
    sfn.reduce()
    return sfn.raw_form()


def add_snailfish_numbers(numbers):
    sfn = SnailfishNumber(numbers[0])
    for number in numbers[1:]:
        sfn = sfn + SnailfishNumber(number)

    return sfn.raw_form()


def reduce_from_file(filename):
    with open(filename) as f:
        lines = [eval(line) for line in f.readlines()]

    sfn = SnailfishNumber(lines[0])
    sfn.reduce()

    for line in lines[1:]:
        sfn = sfn + SnailfishNumber(line)
        sfn.reduce()

    return sfn.raw_form()
