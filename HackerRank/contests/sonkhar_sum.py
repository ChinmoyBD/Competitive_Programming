n = int(input())

while True:
    if n <= 9:
        print(n)
    else:
        count = 0

        while n > 0:
            count += n % 10
            n //= 10
        n = count
        print(n)

    if n <= 9:
        break
