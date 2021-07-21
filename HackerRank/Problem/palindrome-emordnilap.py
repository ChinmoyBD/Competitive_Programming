s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

sum1 = s1 + s2 + s3
sum2 = s2 + s1 + s3
sum8 = s1 + s3 + s2
sum5 = s1 + s2 + s3[::-1]
sum6 = s2[::-1] + s1 + s3
sum7 = s2 + s1[::-1] + s3

sum3 = s1[::-1] + s2[::-1] + s3[::-1]
sum4 = s2[::-1] + s1[::-1] + s3[::-1]
sum9 = s1[::-1] + s3[::-1] + s2[::-1]
if sum1 == sum1[::-1]:
    print("YES")
elif sum2 == sum2[::-1]:
    print("YES")
elif sum3 == sum3[::-1]:
    print("YES")
elif sum4 == sum4[::-1]:
    print("YES")
elif sum5 == sum5[::-1]:
    print("YES")
elif sum6 == sum6[::-1]:
    print("YES")
elif sum8 == sum8[::-1]:
    print("YES")
elif sum7 == sum7[::-1]:
    print("YES")
elif sum9 == sum9[::-1]:
    print("YES")

else:
    print("NO")