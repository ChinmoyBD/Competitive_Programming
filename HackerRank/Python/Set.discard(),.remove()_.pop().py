n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    prd = input().split()
    if prd[0] == "pop":
        s.pop()

    elif prd[0] == "remove":
        s.remove(int(prd[1]))

    elif prd[0] == "discard":
        s.discard(int(prd[1]))

print(sum(s))