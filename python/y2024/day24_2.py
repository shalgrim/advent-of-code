from y2024.day24_1 import process_input, run_machine_on_input


def build_small_machine(i, gates_by_outwire):
    initial_gates = [gates_by_outwire[f"z{j:02}"] for j in range(i + 1)]
    subset_of_gates = initial_gates
    gates_to_get = []
    for gate in subset_of_gates:
        inwires = [
            inwire
            for inwire in gate.inwires
            if not (inwire.startswith("x") or (inwire.startswith("y")))
        ]
        for inwire in inwires:
            gates_to_get.append(inwire)

    while gates_to_get:
        for outwire in gates_to_get:
            if outwire in gates_by_outwire:  # xs and ys aren't in here
                subset_of_gates.append(gates_by_outwire[outwire])

        gates_to_get = []
        outwires_we_have = [gate.outwire for gate in subset_of_gates]
        for gate in subset_of_gates:
            inwires = [
                inwire
                for inwire in gate.inwires
                if not (inwire.startswith("x") or (inwire.startswith("y")))
            ]
            for inwire in inwires:
                if inwire not in outwires_we_have:
                    gates_to_get.append(inwire)

    return subset_of_gates


def run_small_machine(small_machine, x, y, highest_xyz_wire_number):
    wires = {}
    for i in range(highest_xyz_wire_number + 1):
        wires[f"x{i:02}"] = 0
        wires[f"y{i:02}"] = 0
    binx = bin(x)
    for i, c in enumerate("".join(reversed(binx))[:-2]):
        wires[f"x{i:02}"] = int(c)
    biny = bin(y)
    for i, c in enumerate("".join(reversed(biny))[:-2]):
        wires[f"y{i:02}"] = int(c)

    return run_machine_on_input(small_machine, wires)


def validate_gates(new_gates, i):
    assert len(new_gates) == 5, (
        f"Should be five new gates, instead got {len(new_gates)}"
    )
    # First gate should be xII XOR yII -> one_of_zII's_inputs
    first_gate_candidates = [
        gate for gate in new_gates if gate.outwire == f"z{i:02}" and gate.tipe == "XOR"
    ]
    assert len(first_gate_candidates) == 1, (
        f"Did not find expected gate foo XOR bar -> z{i:02}"
    )
    first_gate = first_gate_candidates[0]

    # Second gate should be xII XOR YII -> one of the first gate's inwires
    second_gate_candidates = [
        gate
        for gate in new_gates
        if gate.outwire in first_gate.inwires
        and sorted(gate.inwires) == [f"x{i:02}", f"y{i:02}"]
        and gate.tipe == "XOR"
    ]
    assert len(second_gate_candidates) == 1, (
        "Did not find expected second gate xi XOR yi -> one_of_first_gate's_inwires"
    )
    second_gate = second_gate_candidates[0]
    exhausted_first_gate_inwire_index = first_gate.inwires.index(second_gate.outwire)
    other_first_gate_inwire_index = 1 if exhausted_first_gate_inwire_index == 0 else 0

    # Third gate should be an OR gate going into the other inwire of first gate
    third_gate_candidates = [
        gate
        for gate in new_gates
        if gate.outwire == first_gate.inwires[other_first_gate_inwire_index]
        and gate.tipe == "OR"
    ]
    assert len(third_gate_candidates) == 1, (
        "Did not find expected gate foo OR bar -> other_first_gate's_inwire"
    )
    third_gate = third_gate_candidates[0]

    # Fourth gate should be xi-1 AND yi-1 -> one of the third gate's inwires
    fourth_gate_candidates = [
        gate
        for gate in new_gates
        if gate.outwire in third_gate.inwires
        and sorted(gate.inwires) == [f"x{i - 1:02}", f"y{i - 1:02}"]
        and gate.tipe == "AND"
    ]
    assert len(fourth_gate_candidates) == 1, (
        "Did not find expected gate xi-1 AND yi-1 -> one_of_third_gate's_inwires"
    )
    fourth_gate = fourth_gate_candidates[0]
    exhausted_third_gate_inwire_index = third_gate.inwires.index(fourth_gate.outwire)
    other_third_gate_inwire_index = 1 if exhausted_third_gate_inwire_index == 0 else 0

    # Fifth and final gate should be another AND gate that goes into the other third gate inwire
    # NB: The inputs here would be the outputs of gates 2 and 3 from the previous set of newly introduced gates
    fifth_gate_candidates = [
        gate
        for gate in new_gates
        if gate.outwire == third_gate.inwires[other_third_gate_inwire_index]
        and gate.tipe == "AND"
    ]
    assert len(fifth_gate_candidates) == 1, (
        "Did not find expected gate foo AND bar -> other_third_gate's_inwires"
    )
    fifth_gate = fifth_gate_candidates[0]


def main(lines):
    _, gates = process_input(lines)
    gates_by_outwire = {g.outwire: g for g in gates}

    # This approach is probably too big to work
    # But I'm hoping I find an early ish error
    # And then from there I can find things that are wrong by analyzing with
    # each addition of Z how the new gates that are introduced are set up
    # ...
    # So the first error I found was when i == 11 the first addition goes wrong
    # So next I want to try to look at which new gates get added each time
    # ...
    # Try switching this pair: mgj, qnw .. that didn't work
    # Try this pair: qnw, qff...that one works
    # Try this pair: pbv, z16...also seems good
    # Try this pair: qqp, z23...also seems good
    # Try the final pair: fbq, z36...also seems good
    # So then my answer is: fbq,pbv,qff,qnw,qqp,z16,z23,z36
    old_small_machine = []
    for i in range(46):
        small_machine = build_small_machine(i, gates_by_outwire)
        print(f"{i=}")
        print("New Gates:")
        new_gates = [gate for gate in small_machine if gate not in old_small_machine]
        for gate in new_gates:
            print(gate)
        if i > 2:
            try:
                validate_gates(new_gates, i)
            except AssertionError as e:
                print(e)
                print(f"Skipping the rest of {i=}")
                old_small_machine = small_machine
                continue

        running_all_the_numbers = True if i >= 44 else False
        # running_all_the_numbers = False
        if running_all_the_numbers:
            biggest_number = 2 ** (i + 1) - 1
            for x in range(biggest_number):
                y = biggest_number - x
                print(x, y)
                answer = run_small_machine(small_machine, x, y, i)
                try:
                    assert answer == x + y
                except AssertionError:
                    print(f"Error: {i=} {x=} {y=} {x+y=} {answer=}")
                    raise
        old_small_machine = small_machine


if __name__ == "__main__":
    with open("../../data/2024/input24_with_switches.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    # x00 and y00 xoring to z00 seems perfect

    # z01
    # tcd XOR bwv -> z01
    # y01 XOR x01 -> tcd
    # y00 AND x00 -> bwv
    # So if both y00 and x00 are on XOR (y01 XOR x01) are on it will work
    # Which also seems right
    ...

    # z02
    # frj XOR hqq -> z02  # So you can kind of see a pattern here where there's always an XOR going in to a z
    # y02 XOR x02 -> frj  # And the corresponding x and y XOR into something that goes straight into that z XOR
    # sgv OR wqt -> hqq
    # y01 XOR x01 -> tcd  # The 01s will always XOR into tcd
    # x01 AND y01 -> wqt  # The 01s will always AND into wqt
    # y00 AND x00 -> bwv  # The 00s will always AND into bwv
    # y00 XOR x00 -> z00  # The 00s will always XOR into z00
    # tcd XOR bwv -> z01  # Another XOR into a z
    # bwv AND tcd -> sgv  # And then those two will always AND into sgv

    # Hm, I think I just need to add things together and see what's wrong
