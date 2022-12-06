def main(text):
    for i in range(len(text)):
        slice = text[i:i+4]
        if len(set(slice)) == 4:
            return i + 4


if __name__ == '__main__':
    with open('../../data/2022/input06.txt') as f:
        text = f.read().strip()
    print(main(text))
    # print(main('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))
