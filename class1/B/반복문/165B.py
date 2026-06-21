# 현재 돈을 100엔 가지고 있다. 연간 이자율은 1%이다. x엔에 도달하기 위해 몇년이 걸리는지 결과를 출력하라.

money = 100
n = 0.01
x = int(input()) # 103 입력
count = 0

while True:
   money += money*x
   count += 1
   if money >= x:
      print(count)
      break