# 133A => n명의 인원, A 비용, 택시 요금은 B

# N,A,B(4, 2, 9)

n,a,b = map(int,input().split())

if n*a > b:
    print(b)
else:
    print(n*a)