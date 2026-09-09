# 2068 최대수 구하기
n = int(input())

for i in range(n):
    matrix = list(map(int,input().split()))
    print(f"#{i+1} {max(matrix)}")