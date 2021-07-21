t = int(input())
for _ in range(t):
    prime = []
    div = []
    x, k = map(int, input().split())
    a = x + k
    rr = a // 3

    for i in range(1, rr+1):
        print(i)
        if a % i == 0:
            div.append(i)
    if a % 2 == 0:
        div.append(a//2)
    div.append(a)

    for j in div:
        if j == 2:
            prime.append(j)
        elif j % 2 == 0:
            continue
        elif j == 3:
            prime.append(j)
        if j > 4:
            pp = True
            for p in range(2, (j//3)+1):
                if j % p == 0:
                    pp = False
                    break
            if j is pp:
                prime.append(j)
    print(div)
    print(prime)
    if x == len(div) and k == len(prime):
        print(1)
    else:
        print(0)
