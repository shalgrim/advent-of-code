def produce_sub_line(nums):
    answer = []
    for i in range(1, len(nums)):
        answer.append(nums[i] - nums[i - 1])
    return answer


def get_next_num(nums):
    if all(n == 0 for n in nums):
        return 0
    return nums[-1] + get_next_num(produce_sub_line(nums))


def main(lines):
    num_lines = []
    for line in lines:
        num_lines.append([int(n) for n in line.split()])
    return sum(get_next_num(nums) for nums in num_lines)


if __name__ == "__main__":
    with open("../../data/2023/input09.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
