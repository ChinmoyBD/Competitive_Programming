
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        sqr = int(i ** 0.5)
        if i != sqr*sqr:
            print("YES")
            break
    else:
        print("NO")


'''
n = 10
pfn = [False] * (n+1)

for i in range(1, n):
    count = 0
    for j in range(i, n+1):
        count += j
        print(count)
        if i == count:
            continue

        if count <= 10:
            pfn[count] = True
        else:
            break
pfn2 = []
pfn3 = []
for o in range(1, n+1):
    if pfn[o] is True:
        pfn2.append(o)
    else:
        pfn3.append(o)
print(pfn2)
print(pfn3)

for _ in range(int(input())):
    l, r = map(int, input().split())
    rm = 1
    tm = r
    r -= l-1
    while rm <= tm:
        if l <= rm <= tm:
            r -= 1
        rm *= 2
    print(r)
'''