n = int(input())
s = input()

count = 0
xxx = []
sub_s = 0

for i in s:
    if i == 'x':
        sub_s += 1
    else:
        xxx.append(sub_s)
        sub_s = 0
xxx.append(sub_s)

for x in xxx:
    if x > 2:
        count += x - 2

print(count)