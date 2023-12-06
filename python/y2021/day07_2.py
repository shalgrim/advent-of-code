def calc_cost(distance):
    """
    distance = 1; answer = 1
    distance = 2; answer = 3 (distance + 1) * (distance / 2)
    distance = 3; answer = 6
    distance = 4; answer = 10 (distance + 1) * (distance / 2)
    distance = 5; answer = 15
    distance = 6; answer = 21 (distance + 1) * (distance / 2)
    """
    if distance == 1:
        return 1
    if distance % 2 == 1:
        return calc_cost(distance-1) + distance
    return (distance + 1) * (distance // 2)


def main(txt):
    positions = [int(i) for i in txt.split(',')]
    cost_to_move = {}
    print(min(positions), max(positions))

    for final_position in range(min(positions), max(positions)+1):
        print(f'{final_position=}')
        cost_to_move[final_position] = sum([calc_cost(abs(final_position - i)) for i in positions])

    return min(cost_to_move.values())


if __name__ == '__main__':
    with open('../data/input06.txt') as f:
        txt = f.read()
    print(main(txt))
