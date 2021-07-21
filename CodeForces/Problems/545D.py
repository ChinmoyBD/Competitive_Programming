n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(n-1):
    index_min = i
    for j in range(i+1, n):
        if arr[index_min] > arr[j]:
            index_min = j

    if i != index_min:
        arr[i], arr[index_min] = arr[index_min], arr[i]
        count += 1
print(count)