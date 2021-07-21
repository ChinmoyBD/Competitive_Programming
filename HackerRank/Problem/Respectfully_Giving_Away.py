t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    m = max(arr)

    if arr.count(m) == 1:
        print("Yes")
    else:
        print("No")