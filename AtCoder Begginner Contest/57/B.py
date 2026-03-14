# B - Checkpoints

a,b=map(int,input().split())
matrix1 = []
matrix2 = []
res = []

for i in range(a):
    matrix1.append(list(map(int,input().split())))

for i in range(b):
    matrix2.append(list(map(int,input().split())))

for i in range(a):
    for j in range(b):
        x = abs(matrix1[i][0] - matrix2[j][0])
        y = abs(matrix1[i][1] - matrix2[j][1])
        res.append(x+y)
    print(res.index(min(res))+1)
    res = []

# map 결과를 진짜 리스트로 만들어서 저장하려면 반드시 list()로 한 번 더 감싸줘야함