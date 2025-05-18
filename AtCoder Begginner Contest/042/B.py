# Iroha Loves Strings (ABC Edition)
n, l = map(int,input().split())
matrix = []

for i in range(n):
    matrix.append(input())

matrix.sort()

for i in range(n):
    print(matrix[i],end='')