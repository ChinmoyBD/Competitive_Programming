for _ in range(int(input())):
    arr = list(map(int, input().split()))

    if (arr[0] <= arr[4] and arr[1] <= arr[5] and arr[2] <= arr[6]) and (arr[3] <= sum(arr[4:7])):
        print("YES")
    else:
        print("NO")