def move_head(direction, head):
    if direction == 'R':
        return head[0] + 1, head[1]
    if direction == 'L':
        return head[0] - 1, head[1]
    if direction == 'U':
        return head[0], head[1] - 1
    if direction == 'D':
        return head[0], head[1] + 1


def move_tail(head, tail):
    x_dist = abs(head[0] - tail[0])
    y_dist = abs(head[1] - tail[1])

    # no move
    if x_dist <= 1 and y_dist <= 1:
        return tail

    # vertical move
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            return tail[0], tail[1] + 1
        else:
            return tail[0], tail[1] - 1

    # horizontal move
    if head[1] == tail[1]:
        if head[0] > tail[0]:
            return tail[0] + 1, tail[1]
        else:
            return tail[0] - 1, tail[1]

    # diagonal move
    if head[0] > tail[0]:
        new_x = tail[0] + 1
    else:
        new_x = tail[0] - 1

    if head[1] > tail[1]:
        new_y = tail[1] + 1
    else:
        new_y = tail[1] - 1

    return new_x, new_y


def main(lines):
    head = (0, 0)
    tail = (0, 0)
    points_covered = set()
    points_covered.add(tail)
    for line in lines:
        direction = line.split()[0]
        num_moves = int(line.split()[1])

        for _ in range(num_moves):
            head = move_head(direction, head)
            print(f'{head=}')
            tail = move_tail(head, tail)
            if tail not in points_covered:
                print(f'{tail=}')
                points_covered.add(tail)
    print(f'{points_covered=}')
    return len(points_covered)


if __name__ == '__main__':
    with open('../../data/2022/input09.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))
