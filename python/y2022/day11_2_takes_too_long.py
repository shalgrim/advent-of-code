from y2022.day11_1 import main as main

if __name__ == '__main__':
    with open('../../data/2022/test11.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, 10000, 1))
