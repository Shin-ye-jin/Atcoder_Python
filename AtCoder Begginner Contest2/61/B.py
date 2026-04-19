# B - Counting Roads
# 4 3 도시가 4개, 도로가 3개 있다는 뜻
# 1 2 1번 도시와 2번 도시 사이에 길이 하나 있다.
# 2 3 2번 도시와 3번 도시 사이에 길이 하나 있다.
# 1 4 1번 도시와 4번 도시 사이에 길이 하나 있다.

n,m = map(int,input().split())

matrix = [0]*n

for i in range(m):
    a,b = map(int,input().split())
    matrix[a-1] +=1
    matrix[b-1] +=1

for i in range(n):
    print(matrix[i])