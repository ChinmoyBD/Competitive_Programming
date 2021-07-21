n, m, k = map(int, input().split())
count = 0
for _ in range(n):
    lc = list(map(int, input().split()))
    if sum(lc[:-1]) >= m and lc[-1] <= 10:
        count += 1
print(count)