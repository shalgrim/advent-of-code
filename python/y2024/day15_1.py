from aoc.io import this_year_day


def process_input(lines):
    map = []
    for i, line in enumerate(lines):
        if not line:
            break
        map.append(line)

    moves = "".join(lines[i + 1 :])
    return map, moves


def score_map(map):
    score = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "O":
                score += 100 * y + x

    return score


class Map:
    def __init__(self, lines):
        self.walls = set()
        self.robot = None
        self.boxes = set()

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    self.walls.add((x, y))
                elif char == "O":
                    self.boxes.add((x, y))
                elif char == "@":
                    self.robot = x, y

    def is_position_a_box(self, position):
        return position in self.boxes

    def move(self, move):
        if move == "^":
            next_move = self.robot[0], self.robot[1] - 1
        elif move == "v":
            next_move = self.robot[0], self.robot[1] + 1
        elif move == "<":
            next_move = self.robot[0] - 1, self.robot[1]
        elif move == ">":
            next_move = self.robot[0] + 1, self.robot[1]
        else:
            raise NotImplementedError("Unexpected Move")
        if next_move in self.walls:
            return
        if not self.is_position_a_box(next_move):  # i.e., it's open
            self.robot = next_move
            return
        if move == "^":
            self.move_boxes_up()
        elif move == "v":
            self.move_boxes_down()
        elif move == "<":
            self.move_boxes_left()
        elif move == ">":
            self.move_boxes_right()

    def move_boxes_up(self):
        next_move = self.robot[0], self.robot[1] - 1

        num_boxes = 0
        searching = next_move
        while self.is_position_a_box(searching):
            num_boxes += 1
            searching = searching[0], searching[1] - 1
        if searching in self.walls:  # nothing to be done
            return

        # move the box immediately above robot to searching
        self.boxes.add(searching)
        self.boxes.remove(next_move)
        self.robot = next_move

    def move_boxes_down(self):
        next_move = self.robot[0], self.robot[1] + 1

        num_boxes = 0
        searching = next_move
        while self.is_position_a_box(searching):
            num_boxes += 1
            searching = searching[0], searching[1] + 1
        if searching in self.walls:  # nothing to be done
            return

        # move the box immediately above robot to searching
        self.boxes.add(searching)
        self.boxes.remove(next_move)
        self.robot = next_move

    def move_boxes_left(self):
        next_move = self.robot[0] - 1, self.robot[1]

        num_boxes = 0
        searching = next_move
        while self.is_position_a_box(searching):
            num_boxes += 1
            searching = searching[0] - 1, searching[1]
        if searching in self.walls:  # nothing to be done
            return

        # move the box immediately above robot to searching
        self.boxes.add(searching)
        self.boxes.remove(next_move)
        self.robot = next_move

    def move_boxes_right(self):
        next_move = self.robot[0] + 1, self.robot[1]

        num_boxes = 0
        searching = next_move
        while self.is_position_a_box(searching):
            num_boxes += 1
            searching = searching[0] + 1, searching[1]
        if searching in self.walls:  # nothing to be done
            return

        # move the box immediately above robot to searching
        self.boxes.add(searching)
        self.boxes.remove(next_move)
        self.robot = next_move

    @property
    def score(self):
        return sum(box[0] + 100 * box[1] for box in self.boxes)


def main(lines):
    raw_map, moves = process_input(lines)
    map = Map(raw_map)

    for move in moves:
        map.move(move)

    # return score_map(raw_map)
    return map.score


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/test15_small.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open(f"../../data/{year}/test15_large.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
