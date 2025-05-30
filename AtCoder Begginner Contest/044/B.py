# Beautiful Strings
# n=list(input())
# num=0
# for i in range(len(n)//2):
#     if n[i] == n[len(n)-i-1]:
#         num+=1
#     else:
#         num=0
#         break
#
# if num==0 or len(n)%2==1:
#     print("No")
# else:
#     print("Yes")

from collections import defaultdict

n = input()
matrix = defaultdict(int)

for i in n:
    matrix[i] += 1

for i in matrix.values():
    if i%2:
        print("No")
        exit()
print("Yes")