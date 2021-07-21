def merge_the_tools(string, k):
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]


if __name__ == "__main__":
    string = input().upper().strip()
    k = int(input())

    merge_the_tools(string, k)