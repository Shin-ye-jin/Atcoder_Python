# 127A => 13살 이상이면 B 엔화를 지출, 6살과 12살 사이라면 절반의 비용, 5살 이하 나이는 무료입니다.

# A,B (30, 100)

a,b = map(int,input().split())

if a >= 13:
    print(b)
elif a>=6 and a<=12:
    print(b//2)
else:
    print(0)