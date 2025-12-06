from coding_puzzle_tools import read_input
from y2025.day05_1 import get_ranges


def main(lines: list[str]) -> int:
    _, ranges = get_ranges(lines)
    lowest = min(r[0] for r in ranges)
    highest = max(r[1] for r in ranges)
    ranges = sorted(ranges)
    print(f"{highest=}, {len(ranges)=}")
    answer = ranges[0][1] - ranges[0][0] + 1
    tracker = ranges[0][1] + 1

    for lower, upper in ranges[1:]:
        # case 1 - tracker is within the range
        if lower <= tracker <= upper:
            answer += upper - tracker + 1
        # case 2 - we're already past this range
        elif tracker > upper:
            pass
        # case 3 - tracker is not within the range
        else:
            print(tracker, lower)
            assert tracker < lower
            answer += upper - lower + 1
        tracker = upper + 1

    return answer


if __name__ == "__main__":
    print(main(read_input()))
