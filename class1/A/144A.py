# 두 정수 A와 B가 모두 1부터 9사이의 숫자인지 확인하고 맞다면 곱한 값을 출력, 아니라면 –1을 출력


A, B = map(int, input().split())

if 1 <= A <= 9 and 1 <= B <= 9:
   print(A*B)
else:
   print(-1)