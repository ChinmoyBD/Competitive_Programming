'''
def f(x):
    return int(str(x)[::-1])


def g(x):
    return x // f(f(x))

'''

if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(len(n))