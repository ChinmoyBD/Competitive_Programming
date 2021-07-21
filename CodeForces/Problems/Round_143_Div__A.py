t = int(input())
count = 0
for _ in range(t):
    a, b, c = map(int, input().split())
    test = a+b+c
    if test > 1:
        count += 1
print(count)