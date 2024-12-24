class Gate:
    def __init__(self, line):
        inputt, output = line.split(" -> ")
        self.outwire = output
        isplit = inputt.split()
        self.inwires = [isplit[0], isplit[2]]
        self.tipe = isplit[1]

    def state(self, wires):
        if self.outwire in wires:
            return wires[self.outwire]

        if any(wire not in wires for wire in self.inwires):
            return None
        match self.tipe:
            case "AND":
                answer = wires[self.inwires[0]] & wires[self.inwires[1]]
            case "OR":
                answer = wires[self.inwires[0]] | wires[self.inwires[1]]
            case "XOR":
                answer = wires[self.inwires[0]] ^ wires[self.inwires[1]]
            case _:
                raise ValueError("Should not be here")
        wires[self.outwire] = answer
        return answer


def process_input(lines):
    wires = {}
    gates = []
    for i, line in enumerate(lines):
        if not line:
            break
        wire_name, wire_val = line.split(": ")
        wire_val = int(wire_val)
        wires[wire_name] = wire_val

    for line in lines[i + 1 :]:
        gates.append(Gate(line))

    return wires, gates


def compute_answer(wires):
    zwires = sorted([k for k in wires if k.startswith("z")], reverse=True)
    zvals = [str(wires[wire]) for wire in zwires]
    answer = int("".join(zvals), base=2)
    return answer


def main(lines):
    wires, gates = process_input(lines)
    none_gates = [1 for gate in gates if gate.state(wires) is None]

    # 🤔Checking their states should be enough to turn everything on?
    while none_gates:
        none_gates = [1 for gate in gates if gate.state(wires) is None]

    answer = compute_answer(wires)
    return answer


if __name__ == "__main__":
    with open(f"../../data/2024/test24_1.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
    with open(f"../../data/2024/test24_2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
    with open(f"../../data/2024/input24.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
