import math
from itertools import pairwise
from math import prod
from typing import List

from coding_puzzle_tools import read_input


def main(lines: List[str]) -> int:
    num_rows = len(lines)
    num_columns = max(len(line) for line in lines)
    operators = lines[-1].split()
    operator_indexes = [i for i, c in enumerate(lines[-1]) if c.strip()]
    # operator_indexes.append(num_columns + 1)
    groupings = []
    for index1, index2 in pairwise(operator_indexes):
        groupings.append([])
        for i in range(index1, index2 - 1):
            s = "".join(row[i] for row in lines[:-1])
            s = "".join(s.split())
            groupings[-1].append(int(s))

    # last grouping is a pita
    groupings.append([])
    for i in range(index2, num_columns):
        s = ""
        for row in lines[:-1]:
            if len(row) > i:
                s += row[i]
        s = "".join(s.split())
        groupings[-1].append(int(s))

    answer = 0
    for operator, grouping in zip(operators, groupings):
        if operator == "+":
            answer += sum(grouping)
        elif operator == "*":
            answer += prod(grouping)
        else:
            raise NotImplementedError("Shouldn't happen")
    return answer


if __name__ == "__main__":
    print(main(read_input()))
