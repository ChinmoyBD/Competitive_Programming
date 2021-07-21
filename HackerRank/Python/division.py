def division(a, b):
    dv_int = a//b
    dv_float = a/b
    return ('{}\n{}'.format(dv_int,dv_float))
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(division(a,b))
