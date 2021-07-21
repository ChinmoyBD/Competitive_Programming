def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        _gcd = 1
        gcdSum = n

        while n > gcdSum or _gcd <= 1:
            countSum = 0
            for i in str(gcdSum):
                countSum += int(i)
            _gcd = gcd(gcdSum, countSum)

            if gcdSum >= n and _gcd > 1:
                print(gcdSum)
                break

            gcdSum += _gcd


