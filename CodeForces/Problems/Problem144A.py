n = int(input())
li = list(map(int, input().split()))

min_index = max_index = 0
min_value = max_value = li[0]

for i in range(n):
    if li[i] <= min_value:
        min_value = li[i]
        min_index = i

    if li[i] > max_value:
        max_value = li[i]
        max_index = i

if min_index < max_index:
    print((max_index-1)+(n-min_index)-1)
else:
    print((max_index-1)+(n-min_index))