def countingValleys(n, s):
    co = 0
    count = 0
    for i in s:
        if i == 'U':
            co += 1
        else:
            co -= 1
        if co == 0 and i == 'U':
            count += 1

    return count


if __name__ == "__main__":
    n = int(input())

    s = input().strip()

    print(countingValleys(n, s))