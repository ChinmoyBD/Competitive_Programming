def goodThings(li):
    if len(li) == 1:
        return li[0]*li[0]
    count = 1
    for i in li:
        count *= i

    return count


if __name__ == "__main__":
    n = int(input())

    for _ in range(1, n+1):
        m = int(input())
        li = list(map(int,input().strip().split()))
        print("Case {0}: {1}".format(_, goodThings(li)))