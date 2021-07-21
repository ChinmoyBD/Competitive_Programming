if __name__ == "__main__":
    t = int(input())
    li = []
    for _ in range(t):
        _input = list(input().split())
        if _input[0] == 'insert' or _input[0] == 'append' or _input[0] == 'remove':
            if len(_input) > 1:
                for i in range(1, 3):
                    convert = int(_input[i])
                    _input[i] = convert
                    if _input[0] == 'append' or _input[0] == 'remove':
                        break

        if _input[0] == 'insert':
            li.insert(_input[1], _input[2])
        elif _input[0] == 'print':
            print(li)
        elif _input[0] == 'remove':
            li.remove(_input[1])
        elif _input[0] == 'append':
            li.append(_input[1])
        elif _input[0] == 'sort':
            li.sort()
        elif _input[0] == 'pop':
            li.pop()
        elif _input[0] == 'reverse':
            li.reverse()
