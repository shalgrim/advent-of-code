import time
from aoc.io import this_year_day


def process_stones(stones):
    answer = []
    for stone in stones:
        if stone == "0":
            answer.append("1")
        elif len(stone) % 2 == 0:
            midpoint = len(stone) // 2
            left = stone[:midpoint]
            right = str(int(stone[midpoint:]))
            # right = stone[midpoint:].lstrip("0") or "0"
            answer += [left, right]
        else:
            answer.append(str(int(stone) * 2024))
    return answer


def main(text):
    stones = text.split()
    for i in range(25):
        print(f"{i=}")
        stones = process_stones(stones)
    return len(stones)


if __name__ == "__main__":
    # testing = False
    testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    start_time = time.time()
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        text = f.read().strip()
    print(main(text))
    print("--- %s seconds ---" % (time.time() - start_time))
