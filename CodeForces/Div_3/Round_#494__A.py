arr = [0] * 101

n = int(input())
a = list(map(int, input().split()))

for i in a:
    arr[i] += 1

count = 0
run = True

while run:
    run = False

    for i in range(1, 101):
        if arr[i] > 0:
            arr[i] -= 1
        if arr[i] > 0:
            run = True
    count += 1

print(count)