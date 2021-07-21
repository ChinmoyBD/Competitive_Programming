for _ in range(int(input())):
    n = int(input())
    ns = n*n
    arr = [0] * ns

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        item = 1
        for i in range(0, ns, 2):
            arr[i] = item
            item += 1
        for j in range(1, ns, 2):
            arr[j] = item
            item += 1
        index = 0
        for x in arr:
            print(x, end=' ')
            if index == n-1:
                index = 0
                print()
            else:
                index += 1

