# B - ∵∴∵
# strip() 은 문자열에서 줄바꿈을 없애는 방법이다
import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

matrix=[]
i=0

while len(a)>i or len(b)>i:
    if i<len(a):
        matrix.append(a[i])
    if i<len(b):
        matrix.append(b[i])
    i+=1

res = "".join(matrix)

print(res)