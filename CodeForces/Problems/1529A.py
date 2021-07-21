for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    print(n-arr.count(arr[0]))