t = int(input())
for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    arr = []
    a = 1
    b = 0
    for i in range(n):
        if i == 0:
            arr.append(seq[0])
        elif i % 2 != 0:
            arr.append(seq[n-a])
            b += 1
        else:
            arr.append(seq[b])
            a += 1
    print(*arr)