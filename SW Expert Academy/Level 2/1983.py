# 1983 조교의 성적 매기기
t = int(input())
n, k = map(int,input().split())
avl = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

count = 0

stu = {}
res = []
avl_tmp = []

for i in range(10):
    for j in range(n//10):
        avl_tmp.append(avl[i])

print(avl_tmp)

for i in range(n):
    a,b,c = map(int,input().split())
    stu[i] = a*0.35+b*0.35+c*0.2

for number, score in stu.items():
    res.append(score)

# 역순 정렬

for i in range(n):
    count+=1
    if stu[k-1] == res[i]:
        print(avl_tmp[count-1])

print(res)
print(stu)