def bonAppetit(bill, k, b):
    count = 0
    for i in range(len(bill)):
        if k == i:
            continue
        count += bill[i]
    sub = b - (count // 2)
    if sub == 0:
        print("Bon Appetit")
    else:
        print(sub)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
