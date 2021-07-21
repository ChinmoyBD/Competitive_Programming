dollar = int(input())
count = 0

while dollar > 0:
    if dollar // 100 > 0:
        temp = dollar // 100
        dollar -= temp * 100
        count += temp

    elif dollar // 20 > 0:
        temp = dollar // 20
        dollar -= temp * 20
        count += temp

    elif dollar // 10 > 0:
        temp = dollar // 10
        dollar -= temp * 10
        count += temp

    elif dollar // 5 > 0:
        temp = dollar // 5
        dollar -= temp * 5
        count += temp

    else:
        temp = dollar // 1
        dollar -= temp
        count += temp

print(count)