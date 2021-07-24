from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    arr.sort()

    for i in range(n):
        count -= bisect_left(arr, l-arr[i], i+1)
        count += bisect_right(arr, r-arr[i], i+1)
    print(count)

