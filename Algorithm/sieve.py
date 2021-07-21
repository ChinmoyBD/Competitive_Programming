n = int(input())

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

print(Prime)
