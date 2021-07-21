def covidlq(li):
    count = 0
    co = 0
    for i in li:
        if i == 1 and co != 0 and count < 5:
            return "NO"
        count += 1
        if i == 1:
            co += 1
            count = 0

    return "YES"


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        li = list(map(int, input().strip().split()))

        print(covidlq(li))