def covid_run(n, k, x, y):
    if x == y:
        return "YES"
    for i in range(n):
        x += k
        if x >= n:
            x = 1
        if x == y:
            return "YES"
    return "NO"


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k, x, y = map(int, input().split())
        print(covid_run(n, k, x, y))