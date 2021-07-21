d1, v1, d2, v2, p = list(map(int, input().split()))
days = i = 1
vac = 0

while True:
    if i >= d1:
        vac += v1
    if i >= d2:
        vac += v2
    if vac >= p:
        break
    days += 1
    i += 1
print(days)