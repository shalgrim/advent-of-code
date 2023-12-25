from y2023.day17_1 import main


def get_neighbors_2(node, nodes):
    answer = []

    # get right neighbor
    if node.came_from == "R":
        key = None
    elif node.came_from == "L":
        if node.came_from_num < 3:
            key = (node.x + 1, node.y, "L", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x + 1, node.y, "L", 1)
    answer.append(nodes.get(key))

    # get down neighbor
    if node.came_from == "D":
        key = None
    elif node.came_from == "U":
        if node.came_from_num < 3:
            key = (node.x, node.y + 1, "U", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x, node.y + 1, "U", 1)
    answer.append(nodes.get(key))

    # get left neighbor
    if node.came_from == "L":
        key = None
    elif node.came_from == "R":
        if node.came_from_num < 3 and node.x > 0:
            key = (node.x - 1, node.y, "R", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x - 1, node.y, "R", 1)
    answer.append(nodes.get(key))

    # get up neighbor
    if node.came_from == "U":
        key = None
    elif node.came_from == "D":
        if node.came_from_num < 3 and node.y > 0:
            key = (node.x, node.y - 1, "D", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x, node.y - 1, "D", 1)
    answer.append(nodes.get(key))

    return [a for a in answer if a]  # remove Nones


if __name__ == "__main__":
    with open("../../data/2023/input17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines), get_neighbors_2, 10)
