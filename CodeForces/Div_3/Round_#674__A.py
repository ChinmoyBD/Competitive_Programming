def check_apartments(n, x):
    if n <= 2:
        return 1
    apa = x + 2
    if n <= apa:
        return 2
    floor = 2
    while apa < n:
        apa = (floor*x) + 2
        floor += 1

    return floor


if __name__ == "__main__":
    for _ in range(int(input())):
        n, x = map(int, input().split())
        print(check_apartments(n, x))