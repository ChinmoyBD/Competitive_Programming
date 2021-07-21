def formingMagicSquare(s):
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
             [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
             [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    mini = 2 ** 64
    for brr in magic:
        diff = 0
        for i, j in zip(arr, brr):
            diff += abs(i - j)
        mini = min(diff, mini)


if __name__ == "__main__":
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    print(formingMagicSquare(s))