def _hash(_list):
    _tuple = tuple(_list)
    return hash(_tuple)

if __name__ == '__main__':
    ren = int(input())
    li = list(map(int,input().split()))
    convert = _hash(li)
    print(convert)