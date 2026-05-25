# 199A => a*a + b*b < c*c를 만족하는가? 만족하면 Yes, 그렇지 않으면 No

# A B C(2 2 4)

a,b,c = map(int,input().split())

if a*a + b*b < c*c:
    print('Yes')
else:
    print('No')