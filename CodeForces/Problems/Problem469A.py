def IWBtG(n, x, y):
    levels = [True] * n

    for i in range(1, len(x)):
        levels[x[i]-1] = False
    for j in range(1, len(y)):
        levels[y[j]-1] = False

    for l in levels:
        if l is True:
            return "Oh, my keyboard!"
    return "I become the guy."


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    print(IWBtG(n, x, y))

