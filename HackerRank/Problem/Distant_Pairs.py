nc = input().split()

n = int(nc[0])

c = int(nc[1])

points = []

for _ in range(n):
    points.append(list(map(int, input().rstrip().split())))

le_n = len(points)

co_max = []

for i in range(le_n - 1):
    for j in range(i+1, le_n):
        co_mini = []
        i1, i2 = points[i], points[j]

        if i1[0] > i2[0]:
            co_mini.append(i1[0] - i2[0])
        else:
            co_mini.append(i2[0] - i1[0])
        if i1[0] > i2[1]:
            co_mini.append(i1[0] - i2[1])
        else:
            co_mini.append(i2[1] - i1[0])

        if i1[1] > i2[0]:
            co_mini.append(i1[1] - i2[0])
        else:
            co_mini.append(i2[0] - i1[1])
        if i1[1] > i2[1]:
            co_mini.append(i1[1] - i2[1])
        else:
            co_mini.append(i2[1] - i1[1])

        if i1[0] > i1[1]:
            co_mini.append(i1[0] - i1[1])
        else:
            co_mini.append(i1[1] - i1[0])
        if i2[0] > i2[1]:
            co_mini.append(i2[0] - i2[1])
        else:
            co_mini.append(i2[1] - i2[0])

    co_max.append(min(co_mini))
    print(co_mini)
print(co_max)
print(max(co_max))