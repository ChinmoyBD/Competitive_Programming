def findDigits(n):
    digit = int(n)
    divisor = []

    while n >= 10:
        divisor.append(n % 10)
        n //= 10
    divisor.append(n % 10)

    d_count = 0
    for i in divisor:
        if i == 0:
            continue
        elif digit % i == 0:
            d_count += 1

    return d_count


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        print(findDigits(n))