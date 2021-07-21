import calendar
def Calendar_module(yyyy, mm, dd):

    li = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    day = calendar.weekday(yyyy, mm, dd)
    return li[day]

if __name__ == "__main__":
    mm, dd, yyyy = map(int,input().split())
    ca = Calendar_module(yyyy, mm, dd)
    print(ca)