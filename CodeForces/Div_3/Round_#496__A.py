n = int(input())
arr = list(map(int, input().split()))

li = list()
count = 1
item = arr[0]
cha_ck = True

for i in range(1, n):
    if item < arr[i]:
        count += 1
        cha_ck = True
    else:
        li.append(count)
        count = 1
        cha_ck = False
        if i == n - 1:
            li.append(count)
if cha_ck:
    li.append(count)

print(len(li))
print(*li)