for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    if sum(arr) == x:
        print("NO")
    else:
        print("YES")
        count = 0
        for i in range(n-1):
            count += arr[i]
            if count == x:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count -= arr[i]
                count += arr[i+1]
        print(*arr)

"""
1 2 3 4 5 6
"""