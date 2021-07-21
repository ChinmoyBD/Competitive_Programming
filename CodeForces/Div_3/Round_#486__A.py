n, k = map(int, input().split())
std = list(map(int, input().split()))
ratings = []
index = []

for i in range(n):
    if std[i] not in ratings:
        ratings.append(std[i])
        index.append(i+1)

if len(ratings) < k:
    print("NO")
else:
    print("YES")
    for i in range(k):
        print(index[i], end=' ')