def superReducedString(s):
    li = []
    for i in s:
        if li and li[-1] == i:
            li.pop()
        else:
            li.append(i)

    if len(li) == 0:
        return "Empty String"
    else:
        return ''.join(li)


if __name__  == "__main__":
    s = input()

    print(superReducedString(s))