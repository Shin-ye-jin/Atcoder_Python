# A - Two Rectangels
a,b,c,d = map(int,input().split())

rec1 = a*b
rec2 = c*d

if rec1 > rec2:
    print(rec1)
elif rec1 < rec2:
    print(rec2)
else:
    print(rec1)