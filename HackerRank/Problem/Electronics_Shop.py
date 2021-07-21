def getMoneySpent(keyboards, drives, b):
    count = 0
    for i in keyboards:
        for j in drives:
            co = i + j
            if co == b:
                return co
            elif b >= co > count:
                count = co
    if count == 0:
        return -1

    return count


if __name__ == "__main__":
    bnm = input().split()

    b = int(bnm[0])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    print(getMoneySpent(keyboards, drives, b))