def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x = 10**(a-1)
    y = 10**(b-1)+10**(c-1)
    print(x, y)

'''
ast = int('1' + '0'*(a-1))
    bst = int('1' + '0'*(b-1))
    gc_d = ''
    while len(str(a)) != a and len(str(b)) != b and len(str(gc_d)) != c:
        ch = 0
        gc_d = gcd(ast, bst)
        if len(str(a)) != a and len(str(b)) != b and len(str(gc_d)) != c:
            ast += 1
            if ch > 5:
                bst += 1
                ch = 0
            ch += 1
'''
