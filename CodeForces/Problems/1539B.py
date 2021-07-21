n, q = map(int, input().split())
st = input()
chrArr = [0]

for i in range(n):
    chrArr.append(chrArr[i] + ord(st[i]) - 96)

for _ in range(q):
    l, r = map(int, input().split())
    print(chrArr[r] - chrArr[l-1])
