s = input().upper().strip()

if s == s[::-1]:
    print("Yes! Palindrome!")
else:
    print("Not Palindrome!")