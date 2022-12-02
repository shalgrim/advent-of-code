TEST_INPUT = 'target area: x=20..30, y=-10..-5'
REAL_INPUT = 'target area: x=117..164, y=-140..-89'


def sub_parser(block):
    strings = block[2:].split('..')
    return int(strings[0]), int(strings[1])


def input_parser(txt):
    _, _, xblock, yblock = txt.split()
    left, right = sub_parser(xblock[:-1])
    bottom, top = sorted(sub_parser(yblock))
    return left, right, top, bottom


def is_in_target(x, y, x0, x1, y0, y1):
    return x0 <= x <= x1 and y0 <= y <= y1


def is_past_target(x, x1):
    return x > x1


def hits_target(init_xvel, init_yvel, x0, x1, y0, y1):
    t = 0
    x = 0
    y = 0
    xvel = init_xvel
    yvel = init_yvel

    while not is_past_target(x, x1):
        if is_in_target(x, y, x0, x1, y0, y1):
            return 0
        elif xvel == 0 and x < x0:
            return -1
        elif xvel == 0 and x < x1 and yvel < 0 and y < y0:
            return -1
        else:
            x += xvel
            y += yvel

            yvel -= 1
            if xvel < 0:
                xvel += 1
            elif xvel > 0:
                xvel -= 1

    return 1


def find_x_that_hits_target(y, x0, x1, y0, y1):
    x = 1
    while True:
        result = hits_target(x, y, x0, x1, y0, y1)
        if result == -1:  # undershot
            x += 1
        elif result == 0:  # hit target
            return x
        else:  # overshot
            return None


def find_max_y_that_hits_target(x0, x1, y0, y1):
    y = 0
    answer = 0

    while find_x_that_hits_target(y, x0, x1, y0, y1):
        answer = y
        y += 1

    return answer


def convert_initial_y_vel_to_max_height(max_y_vel):
    y = 0
    yvel = max_y_vel
    while yvel > 0:
        y += yvel
        yvel -= 1
    return y


def main(text):
    _, _, xcoord, ycoord = text.split()
    xcoords = xcoord[2:-1]
    ycoords = ycoord[2:]
    x0 = int(xcoords.split('..')[0])
    x1 = int(xcoords.split('..')[1])
    y0 = int(ycoords.split('..')[0])
    y1 = int(ycoords.split('..')[1])
    x0, x1 = sorted([x0, x1])
    y0, y1 = sorted([y0, y1])
    max_y_vel = find_max_y_that_hits_target(x0, x1, y0, y1)
    return convert_initial_y_vel_to_max_height(max_y_vel)


def will_land_in_range(init_yvel, y1, y0):
    y = 0
    yvel = init_yvel
    while y >= y0:
        if y <= y1:
            # print(y)
            return True
        y += yvel
        yvel -= 1
    return False


# can I turn this into some solvable formula?
# if so, then I can solve for max initial_velocity using -140 <= height <= -89
# Gaussian formula says (n / 2)(first number + last number) = sum, where n is the number of integers
# and of course n is first - last + 1
# oh duh that makes total sense for when there's an odd number because first and last will add up to an even number...sigh
def height(initial_velocity, t):
    first = initial_velocity
    last = initial_velocity - t + 1
    median = 0 if (first - last) % 2 == 1 else (first + last) // 2
    return (first + last) * (t // 2) + median


def height_gaussian(initial_velocity, t):
    """A more straightforward way of calculating height"""
    n = t + 1
    final_velocity = initial_velocity - t
    return n * (initial_velocity + final_velocity) / 2


def height_gaussian_refactored(initial_velocity, t):
    """Wrote this just to make it purely a function of those two variables"""
    return (t + 1) * (2 * initial_velocity - t) / 2


def main2(y1, y2):
    for i in range(-y2):
        if will_land_in_range(i, y1, y2):
            answer = convert_initial_y_vel_to_max_height(i)
    return answer


if __name__ == '__main__':  # 9591 is too low
    # Ugh, I'd like to find the biggest initial velocity that lands at each point -89 to -140
    # then take the max of those values
    # and finding the maximum height reached by that initial velocity is trivial
    # but how do you maximize initial velocity? Seems like you could just keep searching higher and higher and eventually
    # you'd find another one that lands on that number
    # so we need to find max(initial_velocity) where height_gaussian(initial_velocity, t) == -89
    # and how the heck would i do that?
    # Wait, does it turn into a quadratic equation? No, cuz it has two variables
    # start here next https://www.reddit.com/r/adventofcode/comments/rily4v/2021_day_17_part_2_never_brute_force_when_you_can/
    with open('../data/input17.txt') as f:
        txt = f.read().strip()

    # print(main(txt))
    main2(-89, -140)
