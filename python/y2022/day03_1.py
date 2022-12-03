def priority(item):
    raw = ord(item)
    if raw < 97:
        return raw - (ord('A') - 1) + 26
    else:
        return raw - (ord('a') - 1)


def get_shared_item(items):
    halfway = len(items) // 2
    first_items = set(items[:halfway])
    second_items = set(items[halfway:])
    shared = first_items.intersection(second_items).pop()
    return shared


def main(lines):
    answer = 0
    for list_of_items in lines:
        shared_item = get_shared_item(list_of_items)
        prio = priority(shared_item)
        print(prio)
        answer += priority(shared_item)

    return answer


if __name__ == '__main__':
    with open('../../data/2022/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
