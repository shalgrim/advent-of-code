from y2022.day10_1 import get_x_vals


def main(lines):
    x_vals = get_x_vals(lines)
    output_lines = []

    for horizontal_index in range(6):
        left_index = 40 * horizontal_index
        line_x_vals = x_vals[left_index : left_index + 40]
        line = []
        for i, x_val in enumerate(line_x_vals):
            if x_val in (i-1, i, i+1):
                line.append('#')
            else:
                line.append('.')
        output_lines.append(''.join(line))

    for line in output_lines:
        print(line)


if __name__ == '__main__':
    with open('../../data/2022/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    main(lines)
