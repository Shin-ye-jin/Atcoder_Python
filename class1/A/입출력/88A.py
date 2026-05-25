# 088A => 500원짜리를 최대한 많이 쓰고 남은 '잔돈'을 1원짜리(A개)로 다 채울 수 있니? 라는 뜻

# N,A (2018, 218)

n,a = map(int,input().split())

num = n%500

if num <= a:
    print('Yes')
else:
    print('No')