import textwrap

def wrap(string, max_width):
    _tt = textwrap.fill(string, max_width)
    return _tt

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)