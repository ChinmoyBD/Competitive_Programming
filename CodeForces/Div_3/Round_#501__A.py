n, m = map(int, input().split())
arr = [False] * (m+1)
for _ in range(n):
    l, r = map(int, input().split())
    for i in range(l, r+1):
        arr[i] = True
miss = []
count = 0
for b in range(1, m+1):
    if not arr[b]:
        count += 1
        miss.append(b)
print(count)
print(*miss)