for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sumOfArr = sum(arr)
    avr = sumOfArr // n
    if sumOfArr % n != 0:
        print(-1)
    else:
        count = 0
        for i in arr:
            if i > avr:
                count += 1
        print(count)