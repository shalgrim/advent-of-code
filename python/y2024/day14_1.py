from aoc.io import this_year_day


class Robot:
    def __init__(self, line):
        raw_position, raw_velocity = line.split()
        coordinates = raw_position.split("=")[1]
        self.x, self.y = [int(c) for c in coordinates.split(",")]
        vector = raw_velocity.split("=")[1]
        self.vx, self.vy = [int(v) for v in vector.split(",")]

    def move(self, width, height):
        self.x += self.vx
        while self.x < 0:
            self.x += width
        while self.x >= width:
            self.x -= width

        self.y += self.vy
        while self.y < 0:
            self.y += height
        while self.y >= height:
            self.y -= height


def safety_count(robots, room_width, room_height):
    vertical_wall = room_width // 2
    horizontal_wall = room_height // 2

    q1_count = sum(
        1 for robot in robots if robot.x < vertical_wall and robot.y < horizontal_wall
    )
    q2_count = sum(
        1 for robot in robots if robot.x > vertical_wall and robot.y < horizontal_wall
    )
    q3_count = sum(
        1 for robot in robots if robot.x > vertical_wall and robot.y > horizontal_wall
    )
    q4_count = sum(
        1 for robot in robots if robot.x < vertical_wall and robot.y > horizontal_wall
    )
    answer = q1_count * q2_count * q3_count * q4_count
    return answer


def print_robots(robots, room_width, room_height):
    for y in range(room_height):
        line = ""
        for x in range(room_width):
            if num_robots := sum(1 for robot in robots if (x, y) == (robot.x, robot.y)):
                line += str(num_robots)
            else:
                line += "."
        print(line)


def main(lines, room_width, room_height):
    robots = [Robot(line) for line in lines]
    for _ in range(100):
        for robot in robots:
            robot.move(room_width, room_height)

    answer = safety_count(robots, room_width, room_height)
    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    if testing:
        print(main(lines, 11, 7))
    else:
        print(main(lines, 101, 103))
