from typing import Dict, List


class Robot:
    def __init__(self, produces: str, costs: Dict[str, int]):
        self.produces = produces
        self.costs = costs

    def __str__(self):
        answer = f'produces: {self.produces}; costs:'
        for k, v in self.costs.items():
            answer += f'{v} {k}, '
        return answer[:-2]


class Blueprint:
    def __init__(self, line: str):
        """It's a factory"""
        self.robots = {}
        left_colon, right_colon = line.split(':')
        self.id = int(left_colon.split()[-1])
        sentences = right_colon.split('. ')
        for sentence in sentences:
            print(sentence)
            produces = sentence.split()[1]
            ingredients = sentence.split('costs ')[1].split(' and ')
            robot_costs = {}
            for ingredient in ingredients:
                number = int(ingredient.split()[0])
                tipe = ingredient.split()[1]
                robot_costs[tipe] = number
            self.robots[produces] = Robot(produces, robot_costs)


def maximize_geodes(blueprint, minutes):
    resources = {}
    time_passed = 0
    robots = [Robot('ore', {})]
    while time_passed < minutes:
        for robot in robots:
            resources[robot.produces] += 1
        # I feel like I need a State class, and at each point through this loop I can
        # create all the options of states, but hoo boy


def main(lines: List[str]):
    blueprints = [Blueprint(line) for line in lines]
    answers = [maximize_geodes(bp, 24) for bp in blueprints]
    return max(answers)


if __name__ == '__main__':
    with open('../../data/2022/test19.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
