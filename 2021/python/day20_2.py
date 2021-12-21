from day20_1 import extend_image, process_image


def main(lines, flips=False):  # TODO: make flips based on image enhancement algorithm
    image_enhancement_algorithm = lines[0]
    flipped = False

    input_image = lines[2:]

    for i in range(50):
        print(f'round {i}')
        extended_image = extend_image(input_image, flipped=flipped)
        processed_image = process_image(
            extended_image, image_enhancement_algorithm, flipped=flipped
        )
        input_image = processed_image
        if flips and not flipped:
            flipped = True
        else:
            flipped = False
    answer = 0
    for line in processed_image:
        answer += len([c for c in line if c == '#'])
    return answer


if __name__ == '__main__':
    with open('../data/test20.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

    with open('../data/input20.txt') as f:  # 46453 is too high
        lines = [line.strip() for line in f.readlines()]

    print(main(lines, flips=True))
