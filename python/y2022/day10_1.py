def main(lines):
    cycle = 1
    x = 1
    x_vals = [x]

    for line in lines:
        instruction = line.split()[0]
        if instruction == 'addx':
            value = int(line.split()[1])
            x_vals.append(x)
            cycle += 1
            x += value
            x_vals.append(x)
            cycle += 1
        else:
            x_vals.append(x)
            cycle += 1

    print(f'{cycle=}')
    for i, x in enumerate(x_vals):
        print(i, x)

    print(f'{x_vals[19]=}')
    print(f'{x_vals[59]=}')
    print(f'{x_vals[99]=}')
    print(f'{x_vals[139]=}')
    print(f'{x_vals[179]=}')
    print(f'{x_vals[219]=}')

    return (
        20 * x_vals[19]
        + 60 * x_vals[59]
        + 100 * x_vals[99]
        + 140 * x_vals[139]
        + 180 * x_vals[179]
        + 220 * x_vals[219]
    )


if __name__ == '__main__':
    with open('../../data/2022/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
