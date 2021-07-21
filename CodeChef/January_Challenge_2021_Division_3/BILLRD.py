
for _ in range(int(input())):
    n, k, x, y = list(map(int, input().split()))
    if x == y:
        x = y = n
        print(n, n)
    elif x < y:
        arr = [[x + n - y, n], [n, n - y + x], [y - x, 0], [0, y - x]]
    else:
        arr = [[n, y + n - x], [y + n - x, n], [0, x - y], [x - y, 0]]
    if x != y:
        print(*arr[(k-1) % 4])