year = int(input())

while True:
    year += 1

    d1 = year // 1000
    d2 = (year//100) % 10
    d3 = (year//10) % 10
    d4 = year % 10

    if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
        break
print(year)