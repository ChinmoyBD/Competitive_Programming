
def timeConversion(s):
    s = s.upper().strip()
    if s == '12:00:00AM':
        return '00:00:00'

    elif s == '12:00:00PM':
        return '12:00:00'

    elif s[0:2] != '12' and s[-2] == 'P':
        p = str(int(s[:2]) +12)
        for i in range(2, 8):
            p += s[i]
        return p

    else:
        if s[0:2] == '12' and s[-2] != 'P':
            a = '00'
            for i in range(2, 8):
                a += s[i]
            return  a
        else:
            a = ''
            for i in range(8):
                a += s[i]
            return a



if __name__ == '__main__':


    s = input()

    result = timeConversion(s)
    print(result)
