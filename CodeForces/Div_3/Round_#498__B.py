n, k = map(int, input().split())
nth_p = list(map(int, input().split()))
sor = sorted(nth_p)
ods = []
count = od_max = tp_co = 0

for i in range(n-1, n-k-1, -1):
    count += sor[i]
    i_n = nth_p.index(sor[i])
    ods.append(i_n)
    nth_p[i_n] = -1

print(count)
ods.sort()
ods = [-1]+ods
for i in range(1,len(ods)-1):
    print(ods[i]-ods[i-1], end=' ')
print(n-ods[-2]-1)

