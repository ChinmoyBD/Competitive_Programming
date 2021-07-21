def sell_price(n, li):
    price = 0
    year = 0
    li = sorted(li)[::-1]
    for i in li:
        if i == 0:
            continue
        tp_price = i - year
        if tp_price < 0:
            tp_price = 0

        price += tp_price
        year += 1

    return price


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        li = list(map(int, input().strip().split()))

        print(sell_price(n, li))