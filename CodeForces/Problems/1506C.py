
for _ in range(int(input())):
    a = input()
    b = input()
    lenA = len(a)
    lenB = len(b)

    count = 0
    for i in range(lenA):
        for j in range(lenA):
            if a[i:j+1] in b and (j - i+1) > count:
                count = j - i+1
    print(lenB+lenA - count*2)

