def weightedUniformStrings(s, queries):
    ans = []
    l = len(s)
    x = [0] * l
    for i in range(l):
        if i != 0 and s[i-1] == s[i]:
            x[i] = x[i-1] + ord(s[i]) - 96
        else:
            x[i] = ord(s[i]) - 96
    for n in queries:
        if n in x:
            ans.append("Yes")
        else:
            ans.append("No")
    return ans


if __name__ == "__main__":
    s = input()
    u = int(input())

    q = []

    for _ in range(u):
        q.append(int(input()))

    print(weightedUniformStrings(s, q))