# 106A -> 길이와 너비가 제공된 농장에서 도로의 너비를 제외한다면 남은 면적은 얼마인가?

# A B (2 2)

a,b = map(int,input().split())

a-=1

b-=1

res = a*b

print(res)