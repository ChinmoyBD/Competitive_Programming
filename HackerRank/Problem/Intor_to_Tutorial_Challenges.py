def introTutorial(V, arr):
    index = 0
    for i in arr:
        if i == V:
            return index
        index += 1


if __name__ == "__main__":
    V = int(input())

    n = int(input())

    arr = list(map(int, input().split()))

    print(introTutorial(V, arr))