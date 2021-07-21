t = int(input())
for _ in range(1, t + 1):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(map(int, input().split())))

    column = []
    k = 0
    k_sum = 0
    r = 0
    c = 0
    for i in arr:
        k_sum += i[k]
        k += 1

        for j in range(1, n+1):
            ri = i.count(j)
            if ri > 1:
                r += 1
                break

    for i in range(n):
        l = []
        for j in arr:
            l.append(j[i])
        column.append(l)

    for i in column:
        for j in range(1, n+1):
            ri = i.count(j)
            if ri > 1:
                c += 1
                break

    print("Case #{}: {} {} {}".format(_, k_sum, r, c))