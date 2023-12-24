from copy import deepcopy


class Map:
    def __init__(self, lines):
        self.path = set()
        self.start = (0, 0)
        self.end = (len(lines[0]) - 1, len(lines) - 1)
        self.height = len(lines)
        self.width = len(lines[0])

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                point = (x, y)
                if y == 0:
                    if c == ".":
                        self.start = point
                        self.path.add(point)
                elif y == len(lines) - 1:
                    if c == ".":
                        self.end = point
                        self.path.add(point)
                else:
                    point = (x, y)
                    if c in ".><^v":
                        self.path.add(point)

        self.walkable = self.path


class State:
    def __init__(self, start):
        self.location = start
        self.path = [start]

    def get_moves(self, map):
        if self.location == map.end:
            return []

        x, y = self.location
        possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1)]

        # the only edge case we should have to worry about
        if y > 0:
            possible_moves.append((x, y - 1))

        possible_moves = [move for move in possible_moves if move in map.walkable]
        answer = [move for move in possible_moves if move not in self.path]
        return answer

    def move(self, point):
        self.location = point
        self.path.append(point)

    def draw(self, map):
        outlines = []
        for y in range(map.height):
            outline = ""
            for x in range(map.width):
                point = x, y
                if point in self.path:
                    outline += "O"
                elif point in map.down:
                    outline += "v"
                elif point in map.up:
                    outline += "^"
                elif point in map.left:
                    outline += "<"
                elif point in map.right:
                    outline += ">"
                elif point in map.path:
                    outline += "."
                else:
                    outline += "#"
            outlines.append(outline)

        for line in outlines:
            print(line)


# TODO: Can DRY by just swapping out State and Map implementation
def main(lines):
    map = Map(lines)
    states = [State(map.start)]
    new_states = []
    completed_states = []
    while any(state.get_moves(map) for state in states):
        # move everybody that can move
        for state in states:
            moves = state.get_moves(map)
            if not moves:
                completed_states.append(state)
            for move in moves:
                new_state = deepcopy(state)
                new_state.move(move)
                new_states.append(new_state)
        states = new_states
        new_states = []

    all_states = completed_states + states
    states_in_final_location = [
        state for state in all_states if state.location == map.end
    ]

    return max(len(state.path) for state in states_in_final_location) - 1


if __name__ == "__main__":
    with open("../../data/2023/input23.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
