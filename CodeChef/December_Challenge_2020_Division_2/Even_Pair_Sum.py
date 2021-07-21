for _ in range(int(input())):
    a, b = map(int, input().split())
    even_a = odd_a = a // 2
    even_b = odd_b = b // 2
    if a % 2 != 0:
        odd_a += 1
    if b % 2 != 0:
        odd_b += 1
    print((even_a * even_b)+(odd_a * odd_b))