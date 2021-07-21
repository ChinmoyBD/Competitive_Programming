def anotherMinimaxProblem(a):
    count = 0
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            co = a[i] - a[i+1]
        else:
            co = a[i+1] + a[i]
        print(co)
        if co > count:
            count = co

    return count


if __name__ == "__main__":
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    print(anotherMinimaxProblem(a))