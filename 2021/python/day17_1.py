def is_in_target(x, y, x0, x1, y0, y1):
    return x0 <= x <= x1 and y0 <= y <= y1


def is_past_target(x, x1):
    return x > x1


def hits_target(xvel, yvel, x0, x1, y0, y1):
    t = 0
    x = 0
    y = 0
    max_y = y

    while not is_past_target(x, x1):
        if is_in_target(x, y, x0, x1, y0, y1):
            return 0
        elif xvel == 0 and x < x0:
            return -1
        elif xvel == 0 and x < x1 and yvel < 0 and y < y1:
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


if __name__ == '__main__':
    with open('../data/input17.txt') as f:
        txt = f.read().strip()

    print(main(txt))
