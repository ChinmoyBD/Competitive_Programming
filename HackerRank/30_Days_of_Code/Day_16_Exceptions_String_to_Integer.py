S = input().strip()

try:
    ors = int(S)
    print(ors)

except ValueError:
    print("Bad String")