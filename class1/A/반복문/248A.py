# 123456789처럼 0~9 중 숫자 하나만 빼고 9자리가 무작위로 입력됨. 빠진 숫자가 뭔지 찾아내기

S = input()

# 0부터 9까지 돌면서 빠진 것 찾기

for i in range(10):
   if str(i) not in S:
      print(i)