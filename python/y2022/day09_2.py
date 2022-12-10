from y2022.day09_1 import move_head, move_tail


def main(lines):
    snake = [(0, 0)] * 10
    points_covered = set()
    points_covered.add(snake[-1])
    for line in lines:
        direction = line.split()[0]
        num_moves = int(line.split()[1])

        for _ in range(num_moves):
            snake[0] = move_head(direction, snake[0])
            for snindex in range(1, 10):
                snake[snindex] = move_tail(snake[snindex - 1], snake[snindex])
            if snake[-1] not in points_covered:
                print(f'{snake[-1]=}')
            points_covered.add(snake[-1])
    print(f'{points_covered=}')
    return len(points_covered)


if __name__ == '__main__':
    with open('../../data/2022/input09.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))
