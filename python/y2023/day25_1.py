import itertools
from copy import deepcopy


class Component:
    def __init__(self, key):
        self.key = key
        self.connected = set()


def build_components(lines):
    components = {}
    wires = []
    for line in lines:
        lh, rh = line.split(":")
        key = lh.strip()
        if key not in components:
            components[key] = Component(key)
        for rcomponent in rh.split():
            if rcomponent not in components:
                components[rcomponent] = Component(rcomponent)
            components[key].connected.add(rcomponent)
            components[rcomponent].connected.add(key)
            wires.append(f"{key}:{rcomponent}")
    return components, wires


def _create_reachable_set(components, key):
    answer = set()
    answer.add(key)

    while True:
        newset = set()

        # TODO: Gonna be a lot of repeats here, fix that
        for setkey in answer:
            newset.update(components[setkey].connected)
        newanswer = answer.union(newset)
        if len(newanswer) == len(answer):
            break
        answer = newanswer

    return answer


def create_reachable_sets(components):
    sets = []
    for key, component in components.items():
        if any(key in s for s in sets):
            continue
        sets.append(_create_reachable_set(components, key))
    return sets


def remove_wires(components, combo):
    new_components = {k: deepcopy(v) for k, v in components.items()}
    for wire in combo:
        lh, rh = wire.split(":")
        new_components[lh].connected.remove(rh)
        new_components[rh].connected.remove(lh)
    return new_components


def main(lines):
    components, wires = build_components(lines)
    for i, combo in enumerate(itertools.combinations(wires, 3)):
        if i % 1000 == 0:
            print(i)
        # lol this is over 619 million
        component_set = remove_wires(components, combo)
        reachable_sets = create_reachable_sets(component_set)
        if len(reachable_sets) == 2:
            break
    answer = len(reachable_sets[0]) * len(reachable_sets[1])
    return answer


if __name__ == "__main__":
    with open("../data/2023/input25.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
