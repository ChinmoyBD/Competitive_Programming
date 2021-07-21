n, m = map(int, input().split())
dor = list(map(int, input().split()))
room = list(map(int, input().split()))
r_count = 0
room_no = 0
do = index = 0
test = -1

for i in room:
    for d in range(index, n):
        if d > test:
            r_count += dor[d]
            test += 1
        if i <= r_count:
            room_no = r_count - (r_count - i) - do
            index = d
            break
        else:
            do += dor[d]
    print(d + 1, room_no)
