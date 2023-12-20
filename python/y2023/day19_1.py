import re


def create_rule(line):
    rule_part = line.split("{")[1][:-1]
    sub_rules = rule_part.split(",")
    answer = []
    for sub_rule in sub_rules:
        if ":" in sub_rule:
            match = re.match(r"([A-Za-z]+)(<|>)(\d+):([A-Za-z]+)", sub_rule)
            groups = match.groups()
            answer.append((groups[0], groups[1], int(groups[2]), groups[3]))
        else:
            answer.append((sub_rule,))

    return answer


def make_part(line):
    props = line[1:-1].split(",")
    answer = {prop.split("=")[0]: int(prop.split("=")[1]) for prop in props}
    return answer


def process_lines(lines):
    rules = {}
    parts = []

    for i, line in enumerate(lines):
        if not line:
            break
        rules[line.split("{")[0]] = create_rule(line)

    for line in lines[i + 1 :]:
        parts.append(make_part(line))

    return rules, parts


def apply_rule(rule, part):
    for sub_rule in rule:
        if len(sub_rule) == 1:
            return sub_rule[0]
        prop, comparator, val, result = sub_rule
        if (comparator == ">" and part[prop] > val) or (
            comparator == "<" and part[prop] < val
        ):
            return result
    else:
        raise RuntimeError("Should not be here")


def is_accepted(part, rules):
    rule = rules["in"]
    while True:
        result = apply_rule(rule, part)
        if result == "A":
            return True
        if result == "R":
            return False
        rule = rules[result]


def main(lines):
    rules, parts = process_lines(lines)
    accepted = [is_accepted(part, rules) for part in parts]
    answer = 0
    for should_count, part in zip(accepted, parts):
        if should_count:
            answer += sum(part.values())
    return answer


if __name__ == "__main__":
    with open("../../data/2023/input19.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
