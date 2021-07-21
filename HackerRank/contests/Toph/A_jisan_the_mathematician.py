n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Stay Home, Stay Safe!!")
elif n % 3 == 0:
    print("Stay Home!!")
elif n % 5 == 0:
    print("Stay Safe!!")
else:
    print("Don’t Go Outside")