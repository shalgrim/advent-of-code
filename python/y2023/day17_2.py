from y2023.day17_1 import main


def get_neighbors_2(node, nodes):
    answer = []
    if node.came_from_num < 4:
        # it's just the one move _if it's there_
        if node.came_from == "R":
            key = (node.x + 1, node.y, "R", node.came_from_num + 1)
        elif node.came_from == "L":
            key = (node.x - 1, node.y, "L", node.came_from_num + 1)
        elif node.came_from == "U":
            key = (node.x, node.y + 1, "U", node.came_from_num + 1)
        elif node.came_from == "D":
            key = (node.x, node.y - 1, "D", node.came_from_num + 1)
        else:
            raise RuntimeError("Shouldn't be here either")
        answer.append(nodes.get(key))
    else:
        keys = []
        if node.came_from == "R":
            # turn 90 degrees
            keys.append((node.x, node.y - 1, "D", 1))
            keys.append((node.x, node.y + 1, "U", 1))

            # keep going left if possible
            # (may not need to do this check if it's not in nodes...)
            if node.came_from_num < 10:
                keys.append((node.x - 1, node.y, "R", node.came_from_num + 1))

        elif node.came_from == "L":
            # turn 90 degrees
            keys.append((node.x, node.y - 1, "D", 1))
            keys.append((node.x, node.y + 1, "U", 1))

            # keep going right if possible
            # (may not need to do this check if it's not in nodes...)
            if node.came_from_num < 10:
                keys.append((node.x + 1, node.y, "L", node.came_from_num + 1))

        elif node.came_from == "D":
            # turn 90 degrees
            keys.append((node.x - 1, node.y, "R", 1))
            keys.append((node.x + 1, node.y, "L", 1))

            # keep going up if possible
            # (may not need to do this check if it's not in nodes...)
            if node.came_from_num < 10:
                keys.append((node.x, node.y - 1, "D", node.came_from_num + 1))

        elif node.came_from == "U":
            # turn 90 degrees
            keys.append((node.x - 1, node.y, "R", 1))
            keys.append((node.x + 1, node.y, "L", 1))

            # keep going down if possible
            # (may not need to do this check if it's not in nodes...)
            if node.came_from_num < 10:
                keys.append((node.x, node.y + 1, "U", node.came_from_num + 1))
        else:
            raise RuntimeError("Shouldn't be here")

        answer = [nodes.get(key) for key in keys]

    return [a for a in answer if a]  # remove Nones


if __name__ == "__main__":
    with open("../../data/2023/input17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines), get_neighbors_2, 10)
