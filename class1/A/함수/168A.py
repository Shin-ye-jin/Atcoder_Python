# 3이면 “bon”, 0 1 6 8이면 “pon”, 2 4 5 7 9이면 “hon”을 출력해라

def f(number):
   last = number[-1]
   if last in ['2','4','5','7','9']:
      result = "hon"
   elif last in ['0', '1', '6', '8']:
      result = "pon"
   else:
      result = "bon"
   return result

n = input() # 16 입력
final = f(n)
print(final)
