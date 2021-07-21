n = int(input())
li = [0] * 10
arr = list(map(int, input().split()))
for i in arr:
    li[i] += 1
even = 10
for i in range(8, 1, -2):
    if li[i] > 0 and i < even:
        even = i
if even == 10:
    print(-1)
else:
    li[even] -= 1

    res = 0
    for i in range(9, 0, -1):
        if li[i] > 0:
            res = res*10+i

    res = res*10+even
    print(res)



