import os
import time


class Robot:
    def __init__(self, line, id):
        self.id = id
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


def print_robots(robots, room_width, room_height):
    for y in range(room_height):
        line = ""
        for x in range(room_width):
            if num_robots := sum(1 for robot in robots if (x, y) == (robot.x, robot.y)):
                line += str(num_robots)
            else:
                line += "."
        print(line)


def write_robots(robots, room_width, room_height, filename):
    lines = []
    for y in range(room_height):
        line = ""
        for x in range(room_width):
            if any((x, y) == (robot.x, robot.y) for robot in robots):
                line += "X"
            else:
                line += " "
        lines.append(f"{line}\n")
    with open(filename, "w") as f:
        f.writelines(lines)


def hash_robots(robots):
    return tuple([(robot.id, robot.x, robot.y) for robot in robots])


def symmetrical(robots, room_width, room_height):
    for y in range(room_height):
        line = []
        for x in range(room_width):
            if any((robot.x, robot.y) == (x, y) for robot in robots):
                line.append("X")
            else:
                line.append(".")
        if line != line[::-1]:
            return False


def robot_in_every_row(robots, room_height):
    ys = {robot.y for robot in robots}
    return len(ys) == room_height


def main(lines, room_width, room_height):
    robots = [Robot(line, i) for i, line in enumerate(lines)]
    seconds = 0
    loop_detector = {}
    loop_detector[hash_robots(robots)] = 0
    robot_in_every_row_seconds = []
    while True:
        # if seconds % 1_000 == 0:
        # the pattern below is almost 548 + 103 repeating and 573 + 101 repeating
        # but I may have gotten it a bit wrong
        # try printing out just those patterns and see what you get
        # I think the ones to check out are in the 573 + 101 pattern, they're distributed vertically
        # pretty well...the other pattern is striking but kind of bunched up in a few rows
        # that's only like 100 pictures to look at
        # if seconds < 1500:  # 548 573 650 673 753 774 856 875 85? 976 1062
        #     for robot in robots:
        #         robot.move(room_width, room_height)
        #     seconds += 1
        #     continue

        # if symmetrical(robots, room_width, room_height):
        #     return seconds
        # if seconds > 11000:  # known loop between 10k and 11k
        #     return -1
        # blech; make look at every picture where there's a robot in every row
        if robot_in_every_row(robots, room_height):
            robot_in_every_row_seconds.append(seconds)
        if (seconds - 33) % 103 == 0:
            os.system("clear")
            print(f"{seconds} elapsed")
            print_robots(robots, room_width, room_height)
            time.sleep(1.5)
        # time.sleep(0.5)
        for robot in robots:
            robot.move(room_width, room_height)
        seconds += 1
        # 0 and 10403 determined to be the same
        robot_hash = hash_robots(robots)
        if (loop_start := loop_detector.get(robot_hash)) is not None:
            print(f"found loop from {loop_start} to {seconds}")  # 4646
            print(f"{len(robot_in_every_row_seconds)=}")
            break
        loop_detector[robot_hash] = seconds
        # if (seconds - 68) % 101 == 0:
        # write_robots(robots, room_width, room_height, f"robots_{seconds:05}.txt")


# def main(lines, room_width, room_height):
#     robots = [Robot(line) for line in lines]
#     i = 0
#     loop_detector = {}
#     loop_detector[hash_robots(robots)] = 0
#     while True:
#         i += 1
#         if i % 1000 == 0:
#             print(f"{i=}")
#         for robot in robots:
#             robot.move(room_width, room_height)
#         if hash_robots(robots) in loop_detector:
#             loop_start = loop_detector[hash_robots(robots)]
#             print(f"found loop from {loop_start} to {i}")
#             break
#         loop_detector[hash_robots(robots)] = i
#         top_row_robots = [robot for robot in robots if robot.y == 0]
#         if (
#             len({robot.x for robot in top_row_robots}) == 1
#             and top_row_robots[0].x == room_width // 2
#         ):
#             print_robots(robots, room_width, room_height)
#             print(i)
#             time.sleep(2)


if __name__ == "__main__":
    # TODO: Think about trying to find symmetry
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    # year, day = this_year_day(pad_day=True)
    year, day = 2024, 14
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, 101, 103))
