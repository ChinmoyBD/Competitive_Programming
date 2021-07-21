n = int(input())
arr = list(map(int, input().split()))
tempValue = arr[0]
tempIndex = 1

for i in range(1, n):
    if tempValue != arr[i]:
        arr[tempIndex] = arr[i]
        tempValue = arr[i]
        tempIndex += 1

for _ in range(n-tempIndex):
    arr.pop()
print(arr)