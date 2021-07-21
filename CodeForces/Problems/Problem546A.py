def loan_calculator(price, money, bananas):
    total_price = 0
    for i in range(1, bananas+1):
        total_price += price*i

    if total_price > money:
        print(total_price - money)
    else:
        print(0)


if __name__ == "__main__":
    k, n, w = map(int, input().split())
    loan_calculator(k, n, w)