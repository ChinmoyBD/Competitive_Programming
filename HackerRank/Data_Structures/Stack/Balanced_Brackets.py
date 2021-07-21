def isBalanced(s):
    par = list()
    curly = list()
    square = list()

    for ch in s:
        if ch == '(':
            par.append(ch)
        elif ch == ')':
            if not par:
                return 'NO'
            par.pop()

        elif ch == '{':
            curly.append(ch)
        elif ch == '}':
            if not curly:
                return "NO"
            curly.pop()

        elif ch == '[':
            square.append(ch)
        elif ch == ']':
            if not square:
                return "NO"
            square.pop()
    if not par and not curly and not square:
        return "YES"
    return "NO"


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        s = input()

        print(isBalanced(s))