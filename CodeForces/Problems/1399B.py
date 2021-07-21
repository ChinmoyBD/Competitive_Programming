for _ in range(int(input())):
    n = int(input())
    aArr = list(map(int, input().split()))
    bArr = list(map(int, input().split()))

    aMin = aArr[0]
    bMin = bArr[0]
    for m in range(n):
        if aArr[m] < aMin:
            aMin = aArr[m]
        if bArr[m] < bMin:
            bMin = bArr[m]
    count = 0
    for i in range(n):
        count += max(aArr[i]-aMin, bArr[i]-bMin)

    print(count)

