import itertools
import re
from functools import cache

from aoc.io import this_year_day
from y2024.day21_1 import numericize

SHORTEST_PATHS_NUMERIC_PAD = {
    "0": {
        "0": [""],
        "1": ["^<"],
        "2": ["^"],
        "3": ["^>"],
        "4": ["^^<"],
        "5": ["^^"],
        "6": ["^^>"],
        "7": ["^^^<"],
        "8": ["^^^"],
        "9": ["^^^>"],
        "A": [">"],
    },
    "1": {
        "0": [">v"],
        "1": [""],
        "2": [">"],
        "3": [">>"],
        "4": ["^"],
        "5": ["^>", ">^"],
        "6": ["^>>", ">>^"],
        "7": ["^^"],
        "8": ["^^>", ">^^"],
        "9": ["^^>>", ">>^^"],
        "A": [">>v"],
    },
    "2": {
        "0": ["v"],
        "1": ["<"],
        "2": [""],
        "3": [">"],
        "4": ["^<", "<^"],
        "5": ["^"],
        "6": ["^>", ">^"],
        "7": ["^^<", "<^^"],
        "8": ["^^"],
        "9": ["^^>", ">^^"],
        "A": ["v>", ">v"],
    },
    "3": {
        "0": ["v<", "<v"],
        "1": ["<<"],
        "2": ["<"],
        "3": [""],
        "4": ["^<<", "<<^"],
        "5": ["^<", "<^"],
        "6": ["^"],
        "7": ["^^<<", "<<^^"],
        "8": ["^^<", "<^^"],
        "9": ["^^"],
        "A": ["v"],
    },
    "4": {
        "0": [">vv"],
        "1": ["v"],
        "2": ["v>", ">v"],
        "3": [">>v", "v>>"],
        "4": [""],
        "5": [">"],
        "6": [">>"],
        "7": ["^"],
        "8": ["^>", ">^"],
        "9": ["^>>", ">>^"],
        "A": [">>vv"],
    },
    "5": {
        "0": ["vv"],
        "1": ["v<", "<v"],
        "2": ["v"],
        "3": [">v", "v>"],
        "4": ["<"],
        "5": [""],
        "6": [">"],
        "7": ["^<", "<^"],
        "8": ["^"],
        "9": ["^>", ">^"],
        "A": [">vv", "vv>"],
    },
    "6": {
        "0": ["vv<", "<vv"],
        "1": ["v<<", "<<v"],
        "2": ["v<", "<v"],
        "3": ["v"],
        "4": ["<<"],
        "5": ["<"],
        "6": [""],
        "7": ["^<<", "<<^"],
        "8": ["^<", "<^"],
        "9": ["^"],
        "A": ["vv"],
    },
    "7": {
        "0": [">vvv"],
        "1": ["vv"],
        "2": ["vv>", ">vv"],
        "3": ["vv>>", ">>vv"],
        "4": ["v"],
        "5": ["v>", ">v"],
        "6": ["v>>", ">>v"],
        "7": [""],
        "8": [">"],
        "9": [">>"],
        "A": [">>vvv"],
    },
    "8": {
        "0": ["vvv"],
        "1": ["vv<", "<vv"],
        "2": ["vv"],
        "3": ["vv>", ">vv"],
        "4": ["v<", "<v"],
        "5": ["v"],
        "6": ["v>", ">v"],
        "7": ["<"],
        "8": [""],
        "9": [">"],
        "A": [">vvv", "vvv>"],
    },
    "9": {
        "0": ["vvv<", "<vvv"],
        "1": ["vv<<", "<<vv"],
        "2": ["vv<", "<vv"],
        "3": ["vv"],
        "4": ["v<<", "<<v"],
        "5": ["<v", "v<"],
        "6": ["v"],
        "7": ["<<"],
        "8": ["<"],
        "9": [""],
        "A": ["vvv"],
    },
    "A": {
        "0": ["<"],
        "1": ["^<<"],
        "2": ["^<", "<^"],
        "3": ["^"],
        "4": ["^^<<"],
        "5": ["^^<", "<^^"],
        "6": ["^^"],
        "7": ["^^^<"],
        "8": ["^^^<", "<^^^"],
        "9": ["^^^"],
        "A": [""],
    },
}

SHORTEST_PATHS_DIRECTIONAL_PAD = {
    "<": {"<": [""], "v": [">"], ">": [">>"], "^": [">^"], "A": [">>^"]},
    "v": {"<": ["<"], "v": [""], ">": [">"], "^": ["^"], "A": [">^", "^>"]},
    ">": {"<": ["<<"], "v": ["<"], ">": [""], "^": ["^<", "<^"], "A": ["^"]},
    "^": {"<": ["v<"], "v": ["v"], ">": ["v>", ">v"], "^": [""], "A": [">"]},
    "A": {"<": ["v<<"], "v": ["v<", "<v"], ">": ["v"], "^": ["<"], "A": [""]},
}

ENDS_IN_A_PATTERN = re.compile(r".*?A")

my_cache = {}


def get_starter_paths(code):
    shortest_paths = {""}
    answer = 0
    for pair in itertools.pairwise(f"A{code}"):
        new_paths = [
            f"{path}A" for path in SHORTEST_PATHS_NUMERIC_PAD[pair[0]][pair[1]]
        ]
        shortest_paths = {
            "".join(t) for t in itertools.product(shortest_paths, new_paths)
        }
        answer += len(new_paths[0]) + 1

    return shortest_paths, answer


def get_directional_paths(code):
    shortest_paths = {""}
    answer = 0
    for pair in itertools.pairwise(f"A{code}"):
        new_paths = [
            f"{path}A" for path in SHORTEST_PATHS_DIRECTIONAL_PAD[pair[0]][pair[1]]
        ]
        shortest_paths = {
            "".join(t) for t in itertools.product(shortest_paths, new_paths)
        }
        answer += len(new_paths[0]) + 1

    return shortest_paths, answer


@cache
def length_of_shortest_sequence(code, num_directional_robots):
    # global my_cache
    if num_directional_robots == 0:
        return len(code)

    answer = 0
    for match in ENDS_IN_A_PATTERN.findall(code):
        directional_paths, _ = get_directional_paths(match)
        answers_for_match = []
        for dp in directional_paths:
            answer_for_match = length_of_shortest_sequence(
                dp, num_directional_robots - 1
            )
            answers_for_match.append(answer_for_match)
        answer += min(answers_for_match)

    my_cache[(code, num_directional_robots)] = answer
    return answer


def main(lines):
    complexities = []

    # works for 0 but not higher...
    # I'm looking for 28 with 1 and 68 with 2
    num_directional_robots = 25
    for i, line in enumerate(lines):
        numericized = numericize(line)

        starter_paths, _ = get_starter_paths(line)
        starter_lengths = []
        for sp in starter_paths:
            length = length_of_shortest_sequence(sp, num_directional_robots)
            starter_lengths.append(length)

        # length s/b 12 for robots=0, 28 for 1, and 68 for 2 for the first code in the test file
        length = min(starter_lengths)
        print(f"{line=}, {length=}")
        c = numericized * length
        print(f"{c=}")
        complexities.append(c)
        # break  # just testing the first one for now

    return sum(complexities)


# 154115708116294 is too high (but that's what I get with the test file)
if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
