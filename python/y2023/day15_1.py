def hash(s):
    answer = 0
    for c in s:
        answer += ord(c)
        answer *= 17
        answer %= 256

    return answer


def main(text):
    steps = text.split(",")
    hashes = [hash(step) for step in steps]
    return sum(hashes)


if __name__ == "__main__":
    with open("../../data/2023/input15.txt") as f:
        txt = f.read().strip()
    print(main(txt))
