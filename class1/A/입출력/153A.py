# 153A => 몇번 공격을 해야 모든 피를 다 소모시킬 수 있게 하는가?

# H, A(10, 4)

h,a = map(int,input().split())

cnt=0

while h > 0:
    h-=a
    cnt+=1

print(cnt)