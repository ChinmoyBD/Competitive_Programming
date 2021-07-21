def swap_case(_str):
    swap = _str.swapcase()
    return swap


if __name__ == '__main__':
    _str = input()
    result = swap_case(_str)
    print(result)