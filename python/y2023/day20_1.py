class Module:
    def __init__(self, tipe, key, output):
        self.tipe = tipe
        self.key = key
        self.output = [o.strip() for o in output.split(",")]

    def __str__(self):
        return f"{self.tipe} {self.key}"


class BroadcasterModule(Module):
    def __init__(self, key, output):
        super().__init__("broadcaster", key, output)

    @property
    def state(self):
        return "broadcaster"

    def send(self, signal, *args):
        signals_to_send = []
        for o in self.output:
            signals_to_send.append((o, signal, self.key))
        return signals_to_send


class FlipFlopModule(Module):
    def __init__(self, key, output):
        super().__init__("flipflop", key, output)
        self.state = False  # off

    def send(self, signal, *args):
        if signal == "hi":
            return []
        assert signal == "lo"
        if self.state:
            out_signal = "lo"
        else:
            out_signal = "hi"
        self.state = not self.state
        return [(o, out_signal, self.key) for o in self.output]


class ConjunctionModule(Module):
    def __init__(self, key, output):
        super().__init__("conjunction", key, output)
        self.last_pulse = "lo"
        self.input_signals = {}

    @property
    def state(self):
        return tuple(self.input_signals.values())

    def add_input(self, key):
        self.input_signals[key] = "lo"

    def send(self, signal, input_key):
        self.input_signals[input_key] = signal
        if all(v == "hi" for v in self.input_signals.values()):
            outsig = "lo"
        else:
            outsig = "hi"
        return [(o, outsig, self.key) for o in self.output]


class NullModule(Module):
    def __init__(self):
        pass

    def send(self, *args):
        return []


def make_module(line):
    rule_input, output = line.split(" -> ")
    if rule_input == "broadcaster":
        return rule_input, BroadcasterModule(rule_input, output)
    if rule_input[0] == "%":
        key = rule_input[1:]
        return key, FlipFlopModule(key, output)
    if rule_input[0] == "&":
        key = rule_input[1:]
        return key, ConjunctionModule(key, output)
    raise RuntimeError("Why am i here")


def make_modules(lines):
    modules = {}
    for line in lines:
        key, value = make_module(line)
        modules[key] = value

    # set up conjunction inputs
    for k, v in modules.items():
        for o in v.output:
            if o in modules and modules[o].tipe == "conjunction":
                modules[o].add_input(k)

    return modules


class Machine:
    def __init__(self, lines):
        self.modules = make_modules(lines)
        self.lo_sent = 0
        self.hi_sent = 0

    @property
    def state(self):
        return tuple([module.state for module in self.modules.values()])

    def push_button(self):
        lo_sent = 0
        hi_sent = 0
        signals_to_send = [(self.modules["broadcaster"], "lo", None)]
        while signals_to_send:
            module, signal, source = signals_to_send[0]
            if signal == "lo":
                lo_sent += 1
            elif signal == "hi":
                hi_sent += 1
            else:
                raise RuntimeError("Weird signal")
            keys_and_signals_to_send = module.send(signal, source)
            signals_to_send.extend(
                [
                    (self.modules.get(key, NullModule()), value, source)
                    for key, value, source in keys_and_signals_to_send
                ]
            )
            signals_to_send = signals_to_send[1:]
        return lo_sent, hi_sent


def calc_final(i, state, seen_states, sent_counts):
    original_i = seen_states[state]

    original_lo = 0
    original_hi = 0
    for j in range(original_i):
        original_lo += sent_counts[j][0]
        original_hi += sent_counts[j][1]

    repeatable_lo = 0
    repeatable_hi = 0
    for j in range(original_i, i):
        repeatable_lo += sent_counts[j][0]
        repeatable_hi += sent_counts[j][1]

    num_repeats = (1000 - original_i) // (i - original_i)
    repeatable_lo *= num_repeats
    repeatable_hi *= num_repeats

    # calc remainder
    remainder = 1000 - (original_i + (i - original_i) * num_repeats)
    remainder_lo = sum(r[0] for r in sent_counts[:remainder])
    remainder_hi = sum(r[1] for r in sent_counts[:remainder])

    return (original_lo + repeatable_lo + remainder_lo), (
        original_hi + repeatable_hi + remainder_hi
    )


def main(lines):
    machine = Machine(lines)
    seen_states = {}
    sent_counts = []
    for i in range(1000):
        state = machine.state
        if state in seen_states:
            break
        seen_states[state] = i
        lo_sent, hi_sent = machine.push_button()
        sent_counts.append((lo_sent, hi_sent))
    # do something with i and seen_states[machine.state]
    total_lo_sent, total_hi_sent = calc_final(
        i, machine.state, seen_states, sent_counts
    )
    return total_lo_sent * total_hi_sent


if __name__ == "__main__":
    with open("../../data/2023/input20.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
