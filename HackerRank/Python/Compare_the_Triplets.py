
li1 = list(map(int ,input().split()))
li2 = list(map(int ,input().split()))
asum = 0
bsum = 0
for i in range(3):
    if a[i] > b[i]:
        asum += 1
    elif a[i] < b[i]:
        bsum += 1
print(asum, bsum)