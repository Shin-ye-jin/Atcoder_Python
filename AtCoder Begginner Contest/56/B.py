# B - NarrowRectanglesEasy

w,a,b = map(int,input().split())

n = a+w
m = b+w

if n < b:
    print(b-n)
elif m < a:
    print(a - m)
else:
    print(0)