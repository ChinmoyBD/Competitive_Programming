for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    mn = arr[0]
    mx = arr[0]
    for i in range(n):
        if arr[i] < mn:
            mn = arr[i]
        if arr[i] > mx:
            mx = arr[i]

    if mn < 0:
        print("NO")
    else:
        print(f"YES\n{mx+1}")
        for j in range(mx+1):
            if j != mx:
                print(j, end=' ')
            else:
                print(j)