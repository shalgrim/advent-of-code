def score_map(map):
    # search for horizontal line first
    for answer in range(1, len(map)):
        if answer <= len(map) // 2:
            for i, top_index in enumerate(range(answer - 1, -1, -1)):
                bottom_index = top_index + 1 + 2 * i
                top_row = map[top_index]
                bottom_row = map[bottom_index]
                if top_row != bottom_row:
                    break
            else:
                return 100 * answer
        else:
            for i, bottom_index in enumerate(range(answer, len(map))):
                top_index = bottom_index - 1 - 2 * i
                top_row = map[top_index]
                bottom_row = map[bottom_index]
                if top_row != bottom_row:
                    break
            else:
                return 100 * answer

    # search for vertical line
    for answer in range(1, len(map[0])):
        if answer <= len(map[0]) // 2:
            for i, left_index in enumerate(range(answer - 1, -1, -1)):
                right_index = left_index + 1 + 2 * i
                left_column = [row[left_index] for row in map]
                right_column = [row[right_index] for row in map]
                if left_column != right_column:
                    break
            else:
                return answer
        else:
            for i, right_index in enumerate(range(answer, len(map[0]))):
                left_index = right_index - 1 - 2 * i
                left_column = [row[left_index] for row in map]
                right_column = [row[right_index] for row in map]
                if left_column != right_column:
                    break
            else:
                return answer
    raise RuntimeError("No solution found")


def main(text):
    maps = [map.split() for map in text.split("\n\n")]
    return sum(score_map(map) for map in maps)


if __name__ == "__main__":
    with open("../../data/2023/input13.txt") as f:
        text = f.read()
    print(main(text))
