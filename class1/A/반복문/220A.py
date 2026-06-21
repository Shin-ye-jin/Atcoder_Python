# 세 정수 A,B,C가 주어진다. A 이상 B 이하의 숫자 중에서 C의 배수인 숫자를 아무거나 하나 찾아서 출력, 없으면 –1을 출력

A, B, C = map(int,input().split())
ans = -1
# 입력 123 456 100
for i in range(A, B+1):
    if i % C == 0:
       ans = i
       break

print(ans)