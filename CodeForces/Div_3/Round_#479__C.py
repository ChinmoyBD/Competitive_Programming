n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
if k == 0:
    ans = arr[0] - 1
else:
    ans = arr[k-1]
count = 0

for i in range(n):
    if arr[i] <= ans:
        count += 1
if ans < 1 or count != k:
    print('-1')
else:
    print(ans)