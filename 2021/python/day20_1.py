def extend_image(input_image, flipped=False):
    extra_char = '#' if flipped else '.'
    extended_image = []
    extended_image.append(extra_char * (len(input_image[0]) + 4))
    extended_image.append(extra_char * (len(input_image[0]) + 4))
    for line in input_image:
        if flipped:
            extended_image.append('##' + line + '##')
        else:
            extended_image.append('..' + line + '..')
    extended_image.append(extra_char * (len(input_image[0]) + 4))
    extended_image.append(extra_char * (len(input_image[0]) + 4))
    return extended_image


def get_binary_representation(y, x, extended_image, flipped=False):
    square_rep = []
    for my_y in range(y - 1, y + 2):
        line = []
        for my_x in range(x - 1, x + 2):
            if (
                my_y < 0
                or my_x < 0
                or my_y >= len(extended_image)
                or my_x >= len(extended_image[y])
            ):
                line.append('#' if flipped else '.')
            else:
                line.append(extended_image[my_y][my_x])
        square_rep.append(line)
    binary_rep = ''
    for line in square_rep:
        for c in line:
            if c == '.':
                binary_rep += '0'
            else:
                binary_rep += '1'
    return int(binary_rep, 2)


def process_image(image, algorithm, flipped=False):
    processed_image = []
    for y, line in enumerate(image):
        processed_line = []
        for x, c in enumerate(line):
            index = get_binary_representation(y, x, image, flipped=flipped)
            processed_line.append(algorithm[index])
        processed_image.append(''.join(processed_line))

    return processed_image


def main_test(lines):
    image_enhancement_algorithm = lines[0]

    input_image = lines[2:]
    extended_image = extend_image(input_image)
    processed_image = process_image(extended_image, image_enhancement_algorithm)
    extended_image = extend_image(processed_image)
    processed_image = process_image(extended_image, image_enhancement_algorithm)
    answer = 0
    for line in processed_image:
        answer += len([c for c in line if c == '#'])

    return answer


def main(lines):
    image_enhancement_algorithm = lines[0]

    input_image = lines[2:]
    extended_image = extend_image(input_image)
    processed_image = process_image(extended_image, image_enhancement_algorithm)
    extended_image = extend_image(processed_image, flipped=True)
    processed_image = process_image(extended_image, image_enhancement_algorithm, flipped=True)
    answer = 0
    for line in processed_image:
        answer += len([c for c in line if c == '#'])
    return answer


if __name__ == '__main__':
    with open('../data/test20.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main_test(lines))

    with open('../data/input20.txt') as f:
            lines = [line.strip() for line in f.readlines()]

    print(main(lines))
