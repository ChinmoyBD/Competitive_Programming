t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    if n <= 3:
        arr = [[1]*n]*n
    else:
        r = n
        for _ in range(n):
            arr.append([0]*n)
        if n % 2 == 0:
            mid1 = (n // 2) - 1
            mid2 = mid1 + 1
            count = 0
            n -= 1
            for i in range(r):
                if count < mid1:
                    arr[i][count], arr[i][n-count] = 1, 1
                elif count == mid1 or count == mid2:
                    arr[i][mid1], arr[i][mid2] = 1, 1
                else:
                    arr[i][n-count], arr[i][count] = 1, 1
                count += 1
        else:
            n -= 1
            mid1 = (n // 2) - 1
            mid2 = mid1 + 1
            mid3 = mid2 + 1
            count = 0
            for i in range(r):
                if count < mid1:
                    arr[i][count], arr[i][n - count] = 1, 1
                elif count == mid1 or count == mid2 or count == mid3:
                    arr[i][mid1], arr[i][mid2], arr[i][mid3] = 1, 1, 1
                else:
                    arr[i][n - count], arr[i][count] = 1, 1
                count += 1
    for a in arr:
        print(*a)