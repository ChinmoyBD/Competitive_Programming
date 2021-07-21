def match(s, y):
    n = len(s)-1
    m = len(y)
    count = 0
    for i in range(n):
        x = s[i:i+m]
        for j in range(m):
            if x[j] == y[j]:
                count += 1

        if n == i+m-1:
            break

    return count


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        s = input().strip()

        p = input().strip()

        print("Case {}:".format(_ + 1), match(s, p))
