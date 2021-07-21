def hackerrankInString(s):
    h = 'hackerrank'
    a = 0
    for i in range(len(s)):
        if s[i] == h[a]:
            a += 1
            if a >= 10:
                return "YES"
    return "NO"


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        s = input()
        print(hackerrankInString(s))