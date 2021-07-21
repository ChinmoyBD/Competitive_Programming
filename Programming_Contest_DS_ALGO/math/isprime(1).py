def isPrime(n):
    if n <= 1:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1


print(isPrime(99))