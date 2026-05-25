# 202A => 윗 면의 숫자들의 반대 숫자들을 더한 값은?

# 윗 면이 1일 경우 반대 숫자는 6이다.

# a,b,c(1,4,3)

a,b,c = map(int, input().split())

a = 7-a

b = 7-b

c = 7-c

# 위처럼 하지 않고

res = 21 - (a+b+c)

print(res)