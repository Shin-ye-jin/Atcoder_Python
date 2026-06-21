# 주사위 A개를 던져 나올 수 있는 최소 점수는 A점, 최대 점수는 Ax6점이다. 나란히 출력하시오.

a,b = map(int,input().split())
# 2 11 입력

icount = a*1
acount = a*6

if icount <= b and b <= acount:
   print("Yes")
else:
   print("No")
