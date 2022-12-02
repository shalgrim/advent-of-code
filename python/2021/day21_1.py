def main(p1_start, p2_start):
    scores = [0, 0]
    positions = [p1_start-1, p2_start-1]
    next_die_roll = 1
    die_rolls = 0

    while scores[0] < 1000 and scores[1] < 1000:
        print(f'{scores=}')
        total_roll = 0
        for _ in range(3):
            total_roll += next_die_roll
            next_die_roll = 1 if next_die_roll == 100 else next_die_roll + 1

        positions[0] = (positions[0] + total_roll) % 10
        scores[0] += positions[0] + 1

        if scores[0] >= 1000:
            die_rolls += 3
            break

        total_roll = 0
        for _ in range(3):
            total_roll += next_die_roll
            next_die_roll = 1 if next_die_roll == 100 else next_die_roll + 1

        positions[1] = (positions[1] + total_roll) % 10
        scores[1] += positions[1] + 1

        die_rolls += 6

    return min(scores) * die_rolls


if __name__ == '__main__':
    print(main(10, 8))

