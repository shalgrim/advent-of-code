def main(txt):
    positions = [int(i) for i in txt.split(',')]
    cost_to_move = {}
    print(min(positions), max(positions))

    for final_position in range(min(positions), max(positions)+1):
        print(f'{final_position=}')
        cost_to_move[final_position] = sum([abs(final_position - i) for i in positions])

    return min(cost_to_move.values())


if __name__ == '__main__':
    with open('../data/input06.txt') as f:
        txt = f.read()
    print(main(txt))
