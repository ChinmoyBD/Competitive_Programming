def split_and_join(line):
    _split = line.split(" ")
    _join = "-".join(_split)
    return _join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)