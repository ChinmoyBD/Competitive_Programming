n = int(input())
st = input()

ele = st[0]
ele_sum = 0

for i in range(n):
    if i != 0:
        if ele == st[i]:
            ele_sum += 1
    ele = st[i]


print(ele_sum)
