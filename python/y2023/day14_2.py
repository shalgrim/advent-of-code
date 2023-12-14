from y2023.day14_1 import Map

TOTAL_CYCLES = 1_000_000_000


def main(lines):
    map = Map(lines)
    seen_states = {}
    seen_states[map.state] = 0
    map.cycle()
    num_cycles = 1
    while map.state not in seen_states:
        seen_states[map.state] = num_cycles
        map.cycle()
        num_cycles += 1
    start_of_cycle = seen_states[map.state]
    end_of_cycle = num_cycles
    print(f"{start_of_cycle=} {end_of_cycle=}")
    cycle_length = end_of_cycle - start_of_cycle
    remaining_cycles = (TOTAL_CYCLES - start_of_cycle) % cycle_length

    for _ in range(remaining_cycles):
        map.cycle()

    return map.score


if __name__ == "__main__":
    with open("../../data/2023/input14.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
