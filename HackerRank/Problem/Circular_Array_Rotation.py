def circularArrayRotation(a, k, queries):
    for _ in range(k):
        l_to_f = a[-1]
        for i in range(len(a)-1, 0, -1):
            a[i] = a[i-1]
        a[0] = l_to_f

    item = []

    for i in queries:
        item.append(a[i])

    return item


if __name__ == "__main__":
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int,input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    print(circularArrayRotation(a, k, queries))