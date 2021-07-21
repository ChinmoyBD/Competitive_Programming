n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

for i in arr:
    if i >= arr[k-1] and i != 0:
        count += 1

print(count)