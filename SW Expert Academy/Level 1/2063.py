# 중간값 찾기
n = int(input())
matrix = list(map(int,input().split()))

matrix.sort()

print(matrix[n//2])