from typing import List

from y2024.day16_1 import create_nodes, visit_nodes, Node, Direction


def find_next_spear_tips(spear_tip: Node, all_nodes: List[Node]) -> List[Node]:
    """The key here is there could be both a turnable and a movable"""
    answer = []
    # look for turnable
    same_spot_nodes = [
        node for node in all_nodes if node.x == spear_tip.x and node.y == spear_tip.y
    ]
    turnable_nodes = [
        node for node in same_spot_nodes if node.distance == spear_tip.distance - 1000
    ]
    if turnable_nodes:
        answer.append(turnable_nodes[0])

    # look for movable
    subset_of_nodes = [
        node
        for node in all_nodes
        if node.distance == spear_tip.distance - 1 and node.facing == spear_tip.facing
    ]
    movable_nodes = []
    match spear_tip.facing:
        case Direction.N:
            movable_nodes = [
                node
                for node in subset_of_nodes
                if spear_tip.x == node.x and node.y - 1 == spear_tip.y
            ]
        case Direction.S:
            movable_nodes = [
                node
                for node in subset_of_nodes
                if spear_tip.x == node.x and node.y + 1 == spear_tip.y
            ]
        case Direction.W:
            movable_nodes = [
                node
                for node in subset_of_nodes
                if spear_tip.x == node.x - 1 and node.y == spear_tip.y
            ]
        case Direction.E:
            movable_nodes = [
                node
                for node in subset_of_nodes
                if spear_tip.x == node.x + 1 and node.y == spear_tip.y
            ]
    if movable_nodes:
        answer += movable_nodes
    return answer


def main(lines: List[str]) -> int:
    all_nodes, target_coords = create_nodes(lines)
    visit_nodes(all_nodes, target_coords)
    target_nodes = [node for node in all_nodes if (node.x, node.y) == target_coords]
    shortest_distance_to_target = min(node.distance for node in target_nodes)
    spear_tips: List[Node] = [
        node for node in target_nodes if node.distance == shortest_distance_to_target
    ]
    best_tiles = set()
    while spear_tips:
        new_spear_tips = []
        for spear_tip in spear_tips:
            best_tiles.add((spear_tip.x, spear_tip.y))
            new_spear_tips += find_next_spear_tips(spear_tip, all_nodes)
        spear_tips = new_spear_tips
        # NEXT: Stop checking the same spear tips multiple times
        print(f"{len(spear_tips)=}; {len(best_tiles)=}")
    return len(best_tiles)


if __name__ == "__main__":
    with open(f"../../data/2024/test16_1.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open(f"../../data/2024/test16_2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open(f"../../data/2024/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
