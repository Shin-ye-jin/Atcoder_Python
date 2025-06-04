# C - Tak and Cards
n,a = map(int,input().split())
matrix = list(map(int,input().split()))
res1 = []
res2 = []
for i in range(n-1):
    for j in range(i+1,n):
        print("1")
        res1.append(matrix[i]+matrix[j])
        print(matrix[i]+matrix[j])

    for j in range(len(res1)):
        res1.append(matrix[i]+res1[j])
        print(matrix[i]+res1[j])

print(res1)

# 다시...