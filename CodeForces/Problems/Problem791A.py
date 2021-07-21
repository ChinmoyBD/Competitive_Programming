bear, limak = map(int, input().split())

year = 0
while bear <= limak:
    bear = bear*3
    limak = limak*2

    year += 1
print(year)