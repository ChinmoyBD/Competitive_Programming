for _ in range(int(input())):
    n, d = map(int, input().split())
    ages = list(map(int, input().split()))
    days = 0

    if d == 1:
        print(n)
    else:
        risk_p = n_risk_p = 0
        for i in ages:
            if i >= 80 or i <= 9:
                risk_p += 1
            else:
                n_risk_p += 1

        days += risk_p // d
        if risk_p % d != 0:
            days += 1
        days += n_risk_p // d
        if n_risk_p % d != 0:
            days += 1

        print(days)