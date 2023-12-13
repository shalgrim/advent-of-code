def differ_by_one(top_row, bottom_row):
    return len([1 for tc, bc in zip(top_row, bottom_row) if tc != bc]) == 1


def score_map(map):
    # search for horizontal line first
    for answer in range(1, len(map)):
        smudged = False
        if answer <= len(map) // 2:
            for i, top_index in enumerate(range(answer - 1, -1, -1)):
                bottom_index = top_index + 1 + 2 * i
                top_row = map[top_index]
                bottom_row = map[bottom_index]
                smudgeable = differ_by_one(top_row, bottom_row)
                if top_row != bottom_row and smudged:
                    break  # used up our smudge but found another non-match
                elif not smudged and smudgeable:
                    smudged = True  # using up our smudge
                elif top_row != bottom_row and not smudgeable:
                    break  # can't be saved with a smudge
                elif top_row == bottom_row:
                    pass  # all is well
                else:
                    print("What case didn't I consider 1?")
            else:
                if smudged:
                    return 100 * answer
        else:
            for i, bottom_index in enumerate(range(answer, len(map))):
                top_index = bottom_index - 1 - 2 * i
                top_row = map[top_index]
                bottom_row = map[bottom_index]
                smudgeable = differ_by_one(top_row, bottom_row)
                if top_row != bottom_row and smudged:
                    break  # used up our smudge but found another non-match
                elif not smudged and differ_by_one(top_row, bottom_row):
                    smudged = True
                elif top_row != bottom_row and not smudgeable:
                    break  # can't be saved with a smudge
                elif top_row == bottom_row:
                    pass  # all is well
                else:
                    print("What case didn't I consider 2?")
            else:
                if smudged:
                    return 100 * answer

    # search for vertical line
    for answer in range(1, len(map[0])):
        smudged = False
        if answer <= len(map[0]) // 2:
            for i, left_index in enumerate(range(answer - 1, -1, -1)):
                right_index = left_index + 1 + 2 * i
                left_column = [row[left_index] for row in map]
                right_column = [row[right_index] for row in map]
                smudgeable = differ_by_one(left_column, right_column)
                if left_column != right_column and smudged:
                    break  # used up our smudge but found another non-match
                elif not smudged and smudgeable:
                    smudged = True  # using up our smudge
                elif left_column != right_column and not smudgeable:
                    break  # can't be saved with a smudge
                elif left_column == right_column:
                    pass  # all is well
                else:
                    print("What case didn't I consider 3?")
            else:
                if smudged:
                    return answer
        else:
            for i, right_index in enumerate(range(answer, len(map[0]))):
                left_index = right_index - 1 - 2 * i
                left_column = [row[left_index] for row in map]
                right_column = [row[right_index] for row in map]
                smudgeable = differ_by_one(left_column, right_column)
                if left_column != right_column and smudged:
                    break  # used up our smudge and still found a non-match
                elif not smudged and differ_by_one(left_column, right_column):
                    smudged = True  # using up our smudge
                elif left_column != right_column and not smudgeable:
                    break  # can't be saved with a smudge
                elif left_column == right_column:
                    pass  # all is well
                else:
                    print("What case didn't I consider 4?")
            else:
                if smudged:
                    return answer
    raise RuntimeError("No solution found")


def main(text):
    maps = [map.split() for map in text.split("\n\n")]
    return sum(score_map(map) for map in maps)


if __name__ == "__main__":  # 41466 is too low
    with open("../../data/2023/input13.txt") as f:
        text = f.read()
    print(main(text))
