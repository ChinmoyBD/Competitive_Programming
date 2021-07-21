n = int(input())

arr = list(map(int, input().split()))

l = len(arr) - 1

for i in range(l,0, -1):
    print(arr[i], end=' ')

print(arr[0])