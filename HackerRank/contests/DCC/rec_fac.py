def f91(n):
    print(n)
    if n <= 100:
        return f91(f91(n+11))
    if n > 100:
        return n - 10


while True:
    n = int(input())
    if n == 0:
        break
    print("f91({}) = {}".format(n, f91(n)))