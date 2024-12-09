from copy import copy

from aoc.io import this_year_day


def expand(text):
    output = []
    for i, c in enumerate(text):
        if i % 2 == 0:
            file_number = i // 2
            output += [file_number] * int(c)
        else:
            output += "." * int(c)

    return output


def checksum(rearranged):
    values = [i * c for i, c in enumerate(rearranged) if c != "."]
    return sum(values)


def main(text):
    expanded = expand(text)
    print("expanded")
    print(f"{len(expanded)=}")
    rearranged = copy(expanded)
    iteration = 0
    while True:
        iteration += 1
        print(f"{iteration=} of max {len(expanded)=}")
        # find first dot and give it i
        for i, c in enumerate(rearranged):
            if c == ".":
                break

        # find last non-dot and give it j
        for j in range(len(rearranged) - 1, -1, -1):
            if (last_non_dot := rearranged[j]) != ".":
                break

        if i > j:
            break
        rearranged[i] = last_non_dot
        rearranged[j] = "."
    print("rearranged")
    answer = checksum(rearranged)
    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        text = f.read().strip()
    print(main(text))
