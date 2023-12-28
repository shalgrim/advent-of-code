from y2023.day17_1 import main


def get_neighbors_2(node, nodes):
    answer = []
    if node.came_from_num < 4:
        keys = []
        # it's just the one move _if it's there_
        if node.came_from == "R":
            keys = [(node.x - 1, node.y, "R", node.came_from_num + 1)]
        elif node.came_from == "L":
            keys = [(node.x + 1, node.y, "L", node.came_from_num + 1)]
        elif node.came_from == "U":
            keys = [(node.x, node.y + 1, "U", node.came_from_num + 1)]
        elif node.came_from == "D":
            keys = [(node.x, node.y - 1, "D", node.came_from_num + 1)]
        elif node.came_from == "" and node.x == 0 and node.y == 0:
            # initial state
            keys = [(1, 0, "L", 1), (0, 1, "U", 1)]
        else:
            raise RuntimeError("Shouldn't be here either")
        answer += [nodes.get(key) for key in keys]
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


# TODO: Implement the restriction that it must go four even to stop at the end
# and I assume then it means it can only start going in a direction if there are
# four spaces left to go in that direction
# Wait, that latter part is probably already implemented, I just don't visit the, let's say
# right and left nodes if I get to the bottom having only moved 1-3 times downward
# But I very likely do need to make sure my target keys only contain distance_from >= 4
# So those steps would be:
#   1. Alter how target keys are calculated (will need another input argument) DONE
#   2. Verify the tests still work DONE
#   3. Run part 2
#   4. If that doesn't get me the right answer then ensure that those changes didn't break part 1
# Alternately I could just at the end filter out target nodes with distance_from < 4
if __name__ == "__main__":
    with open("../../data/2023/input17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, get_neighbors_2, 10, 4))
