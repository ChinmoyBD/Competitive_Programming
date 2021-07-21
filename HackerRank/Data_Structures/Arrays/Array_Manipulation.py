def arrayManipulation(n, queries):
    a = [0] * (n + 1)
    count = index = 0
    for i in queries:
        a[i[0]-1] += i[2]
        a[i[1]] -= i[2]

    for i in a:
        index += i
        if index > count:
            count = index

    return count


if __name__ == "__main__":
    n, m = map(int, input().split())

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().split())))

    print(arrayManipulation(n, queries))