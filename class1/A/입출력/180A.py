# 180A => 현재 박스에 N개의 공이 있다. A개의 공을 제거한 후 B개의 공을 다시 집어 넣는다.

# N,A,B (100, 1, 2)

n,a,b = map(int,input().split())

res = n-a+b

print(res)