n, k = map(int, input().split())
problems = list(map(int, input().split()))

count = 0
for i in range(n-1, -1, -1):
    if problems[i] <= k:
        problems[i] = 0
        count += 1
    else:
        break
for p in problems:
    if p <= k and p != 0:
        count += 1
    else:
        break

print(count)