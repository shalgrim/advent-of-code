class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


def main(lines):
    raw_nums = [int(line) for line in lines]
    numbers = [Number(n) for n in raw_nums]
    numbers_by_original_index = {i: number for i, number in enumerate(numbers)}

    for original_index in range(len(numbers_by_original_index)):
        number_to_move = numbers_by_original_index[original_index]
        current_index = numbers.index(number_to_move)
        movement = current_index + number_to_move.value
        new_index = movement % (len(numbers) - 1)
        numbers.pop(current_index)
        # if movement < 0:
        #     new_index -= 1
        if new_index == 0:
            numbers.append(number_to_move)
        else:
            numbers.insert(new_index, number_to_move)

    post_move_raw_numbers = [n.value for n in numbers]
    zero_index = post_move_raw_numbers.index(0)
    val1 = post_move_raw_numbers[(zero_index + 1000) % len(post_move_raw_numbers)]
    val2 = post_move_raw_numbers[(zero_index + 2000) % len(post_move_raw_numbers)]
    val3 = post_move_raw_numbers[(zero_index + 3000) % len(post_move_raw_numbers)]
    return val1 + val2 + val3


if __name__ == '__main__':
    with open('../../data/2022/input20.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    answer = main(lines)
    print(answer)
