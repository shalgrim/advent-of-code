"""
target area: x=117..164, y=-140..-89
Known: highest initial velocity that works is 139
"""
from day17_1 import REAL_INPUT, input_parser
from day17_1 import main2 as part_1


def get_ys_and_ticks(y1, y2):
    answer = []
    for init_y_vel in range(-y2):
        y = 0
        ticks = 0
        yvel = init_y_vel
        while y >= y2:
            if y <= y1:
                answer.append((y, ticks))
            y += yvel
            ticks += 1
            yvel -= 1

    return answer


def get_xs_that_work_for_tick(tick, minx, maxx, left, right):
    """
    Find initial x velocities that put x in range at tick
    :param tick: number of ticks
    :param minx: lowest possible initial x velocity
    :param maxx: highest possible x velocity
    :return: answer - all possible initial x velocities that put x in range at time tick
    """
    answer = []
    for init_x in range(minx, maxx + 1):
        xpos = 0
        xvel = init_x
        for _ in range(tick):
            xpos += xvel
            xvel = max(0, xvel - 1)
        if left <= xpos <= right:
            answer.append(init_x)

    return answer


def get_xs_and_ys(ys_and_ticks, x1, x2):
    answer = set()
    for y, tick in ys_and_ticks:
        for x in get_xs_that_work_for_tick(tick, x1, x2):
            answer.add((x, y))

    return answer


def submain(x1, x2, y1, y2):
    ys_and_ticks = get_ys_and_ticks(y1, y2)
    return get_xs_and_ys(ys_and_ticks, x1, x2)


def convert_max_height_to_initial_yvel(max_height):
    initial_velocity = 0
    resulting_height = 0
    while resulting_height < max_height:
        initial_velocity += 1
        resulting_height = (initial_velocity + 1) * initial_velocity / 2
    return initial_velocity


def get_y_ticks(initial_y_vel, top, bottom):
    """
    Given an initial y velocity,
    returns all the ticks of time when the y position will be
    between top and bottom inclusive
    """
    answer = []
    ypos = 0
    yvel = initial_y_vel
    ticks = 0
    while ypos >= bottom:
        ypos += yvel
        ticks += 1
        yvel -= 1
        if bottom <= ypos <= top:
            answer.append(ticks)
    return answer


def find_pairs_that_work_for_initial_yvel(
    left, right, top, bottom, min_init_xvel, max_init_xvel, initial_yvel
):
    print(f'{initial_yvel=}')
    ticks_where_y_is_in_range = get_y_ticks(initial_yvel, top, bottom)
    inner_answer = set()
    for tick in ticks_where_y_is_in_range:
        xs_for_those_ticks = get_xs_that_work_for_tick(
            tick, min_init_xvel, max_init_xvel, left, right
        )
        inner_answer.update({(x, initial_yvel) for x in xs_for_those_ticks})
    return inner_answer


def find_pairs_that_work(left, right, top, bottom):
    highest_possible_y = part_1(top, bottom)
    max_init_yvel = convert_max_height_to_initial_yvel(highest_possible_y)
    min_init_yvel = bottom
    max_init_xvel = right
    min_init_xvel = convert_max_height_to_initial_yvel(left)
    answer = []
    for initial_yvel in range(min_init_yvel, max_init_yvel + 1):
        inner_answer = find_pairs_that_work_for_initial_yvel(
            left, right, top, bottom, min_init_xvel, max_init_xvel, initial_yvel
        )
        answer += inner_answer
    return answer


def main(txt):
    left, right, top, bottom = input_parser(txt)
    pairs_that_work = find_pairs_that_work(
        left,
        right,
        top,
        bottom,
    )
    return len(pairs_that_work)


if __name__ == '__main__':  # 172 is too low
    print(main(REAL_INPUT))
