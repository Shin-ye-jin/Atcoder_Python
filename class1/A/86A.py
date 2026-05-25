# 두 정수 a와 b를 입력받아 두 수의 곱이 짝수(Even)인지 홀수(Odd)인지 판별

a,b = map(int,input().split())

if (a*b)%2 == 0:
   print("Even")
else:
   print("Odd")