def count_substring(_string, _sub_string):
    _count = 0
    for i in range(0, len(_string) - 1):
        s = ''
        s = _string[i:i + len(_sub_string)]
        if s == _sub_string:
            _count += 1

    return _count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
