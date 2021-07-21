def saveThePrisoner(n, m, s):
    first_round = m - (n - (s-1))
    last_round = first_round % n

    if last_round == 0:
        return n

    return last_round


if __name__ == "__main__":
    for _ in range(int(input())):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        print(saveThePrisoner(n, m, s))