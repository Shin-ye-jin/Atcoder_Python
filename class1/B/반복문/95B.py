# 095B -> N개의 종류, X 그람? 가능 만들 종류 나열 개네들을 만들고 남은 것들로 얼마나 더 만들 수 있는가?

# N X
# m1 m2 m3

n,x = map(int,input().split())

matrix = []

for i in range(n):
    m = int(input())
    matrix.append(m)
    x-=m
    n += x//min(matrix)

print(n)