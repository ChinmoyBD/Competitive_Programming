def reverse(x: int) -> int:
    boll = True
    if x < 0:
        x = x - x * 2
        boll = False

    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x //= 10

    if res > 2**31-1:
        return 0

    if boll is not True:
        return res - res * 2

    return res


if __name__ == "__main__":
    n = int(input())

    print(reverse(n))