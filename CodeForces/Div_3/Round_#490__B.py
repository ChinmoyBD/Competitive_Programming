def div(n, st):
    for i in range(1, n+1):
        if n % i == 0:
            st = st[:i][::-1] + st[i:]

    return st


if __name__ == "__main__":
    n = int(input())
    st = input()
    print(div(n, st))