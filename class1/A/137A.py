# 두 정수 A와 B가 주어짐. B가 A의 배수이면 A+B를 하고, 아니면 B-A를 구하는 문제

def check_cal(a,b):
    if b%a == 0:
      return a+b
    else:
      return b-a

A,B = map(int,input().split())

result = check_cal(A,B)
print(result)