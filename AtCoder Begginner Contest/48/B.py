# Betwween a and b...
import sys

a,b,x=map(int,sys.stdin.readline().split())
# cnt=0
# for i in range(a,b+1):
#     if i%x==0:
#         cnt+=1
#
# print(cnt)

print((b//x) - ((a-1)//x)) # 이걸 어찌?!!