n = int(input())
li = list(map(int, input().split()))

size = n
for i in range(n):
    for j in range(i):
        if li[j] == li[i]:
            li[j] = 0
            size -= 1

print(size)
for i in li:
    if i != 0:
        print(i, end=' ')
