from y2024.day16_1 import create_nodes, visit_nodes


def main(lines):
    all_nodes, target_coords = create_nodes(lines)
    visit_nodes(all_nodes, target_coords)
    target_nodes = [node for node in all_nodes if (node.x, node.y) == target_coords]
    shortest_distance_to_target = min(node.distance for node in target_nodes)
    spear_tip = [
        node for node in target_nodes if node.distance == shortest_distance_to_target
    ][0]


if __name__ == "__main__":
    with open(f"../../data/2024/test16_1.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open(f"../../data/2024/test16_2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    # with open(f"../../data/2024/input16.txt") as f:
    #     lines = [line.strip() for line in f.readlines()]
    # print(main(lines))
