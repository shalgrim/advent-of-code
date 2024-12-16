from aoc.io import this_year_day
from y2024.day15_1 import Map


def process_input(lines):
    map = []
    for i, line in enumerate(lines):
        if not line:
            break
        map.append(line)

    moves = "".join(lines[i + 1 :])
    print(f"{len(moves)=}")
    return map, moves


class Box:
    def __init__(self, left, map):
        self.left = left
        self.right = left[0] + 1, left[1]
        self.map = map

    def move_right(self) -> bool:
        next_spot = self.right[0] + 1, self.right[1]
        if next_spot in self.map.walls:
            return False
        if not self.map.is_position_a_box(next_spot):
            self.left = self.right
            self.right = next_spot
            return True
        if self.map.get_box_at(next_spot).move_right():
            self.left = self.right
            self.right = next_spot
            return True
        return False

    def move_left(self) -> bool:
        next_spot = self.left[0] - 1, self.left[1]
        if next_spot in self.map.walls:
            return False
        if not self.map.is_position_a_box(next_spot):
            self.right = self.left
            self.left = next_spot
            return True
        if self.map.get_box_at(next_spot).move_left():
            self.right = self.left
            self.left = next_spot
            return True
        return False

    def move_up(self) -> bool:
        next_left = self.left[0], self.left[1] - 1
        next_right = self.right[0], self.right[1] - 1
        if next_left in self.map.walls or next_right in self.map.walls:
            return False
        if not self.map.is_position_a_box(next_left) and not self.map.is_position_a_box(
            next_right
        ):
            self.left = next_left
            self.right = next_right
            return True
        left_box = self.map.get_box_at(next_left)
        right_box = self.map.get_box_at(next_right)
        if left_box is right_box or right_box is None:
            if left_box.move_up():
                self.left = next_left
                self.right = next_right
                return True
            return False
        if left_box is None:
            if right_box.move_up():
                self.left = next_left
                self.right = next_right
                return True
            return False
        if left_box.move_up() and right_box.move_up():
            self.left = next_left
            self.right = next_right
            return True
        return False

    def move_down(self) -> bool:
        next_left = self.left[0], self.left[1] + 1
        next_right = self.right[0], self.right[1] + 1
        if next_left in self.map.walls or next_right in self.map.walls:
            return False
        if not self.map.is_position_a_box(next_left) and not self.map.is_position_a_box(
            next_right
        ):
            self.left = next_left
            self.right = next_right
            return True
        left_box = self.map.get_box_at(next_left)
        right_box = self.map.get_box_at(next_right)
        if left_box is right_box or right_box is None:
            if left_box.move_down():
                self.left = next_left
                self.right = next_right
                return True
            return False
        if left_box is None:
            if right_box.move_down():
                self.left = next_left
                self.right = next_right
                return True
            return False
        elif left_box.move_down() and right_box.move_down():
            self.left = next_left
            self.right = next_right
            return True
        return False


class Map2(Map):
    def __init__(self, lines):
        self.walls = set()
        self.robot = None
        self.boxes = []
        self.height = len(lines)
        self.width = len(lines[0]) * 2

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    self.walls.add((x * 2, y))
                    self.walls.add((x * 2 + 1, y))
                elif char == "O":
                    self.boxes.append(Box((x * 2, y), self))
                elif char == "@":
                    self.robot = x * 2, y

    def is_position_a_box(self, position):
        return any(position == box.left for box in self.boxes) or any(
            position == box.right for box in self.boxes
        )

    def get_box_at(self, position):
        for box in self.boxes:
            if box.left == position or box.right == position:
                return box
        return None

    def move_boxes_down(self):
        next_move = self.robot[0], self.robot[1] + 1
        box = self.get_box_at(next_move)
        if box.move_down():
            self.robot = next_move

    def move_boxes_up(self):
        next_move = self.robot[0], self.robot[1] - 1
        box = self.get_box_at(next_move)
        if box.move_up():
            self.robot = next_move

    def move_boxes_left(self):
        next_move = self.robot[0] - 1, self.robot[1]
        box = self.get_box_at(next_move)
        if box.move_left():
            self.robot = next_move

    def move_boxes_right(self):
        next_move = self.robot[0] + 1, self.robot[1]
        box = self.get_box_at(next_move)
        if box.move_right():
            self.robot = next_move

    @property
    def score(self):
        return sum(box.left[0] + 100 * box.left[1] for box in self.boxes)

    def __str__(self):
        lines = []
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                if (x, y) in self.walls:
                    line += "#"
                elif (x, y) == self.robot:
                    line += "@"
                elif any(box.left == (x, y) for box in self.boxes):
                    line += "["
                elif any(box.right == (x, y) for box in self.boxes):
                    line += "]"
                else:
                    line += "."
            lines.append(line)
        return "\n".join(lines)


def main(lines):
    raw_map, moves = process_input(lines)
    map = Map2(raw_map)
    print("Initial Map")
    print(map)

    for move in moves:
        map.move(move)

    print("Final Map")
    print(map)
    return map.score


if __name__ == "__main__":
    # The only thing I can think to do is to start DRY'ing this and that might reveal some copypasta bug
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/test15_part2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open(f"../../data/{year}/test15_large.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    # 1477669 is too low
    with open(f"../../data/{year}/input{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
