n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    n = input().split()
    if n[0] == "update":
        s |= set(map(int, input().split()))

    elif n[0] == "intersection_update":
        s &= set(map(int, input().split()))

    elif n[0] == "difference_update":
        s -= set(map(int, input().split()))

    else:
        s ^= set(map(int, input().split()))

print(sum(s))