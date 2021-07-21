n = 10**5

Prime = []
mark = [0] * (n+2)

limit = int(n**0.5) + 2
mark[1] = 1

for i in range(4, n+1, 2):
    mark[i] = 1

Prime.append(2)

for i in range(3, n+1, 2):
    if mark[i] == 0:
        Prime.append(i)

        if i <= limit:
            for j in range(i*i, n+1, i*2):
                mark[j] = 1


def binary_search(L, X):
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == X:
            return 1
        if L[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    return 0


for _ in range(int(input())):
    l = int(input())
    bs = input().strip()
    oCount = zCount = 0
    ck = True
    for i in range(l):
        if bs[i] == '1':
            oCount += 1
        else:
            zCount += 1
        if oCount >= zCount:
            if binary_search(Prime, i+1):
                print("YES")
                ck = False
                break
    if ck:
        if oCount >= zCount:
            print("YES")
        else:
            print("NO")
