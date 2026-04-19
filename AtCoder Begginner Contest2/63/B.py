# B - Varied
# 문자열 안에 똑같은 글자가 하나라도 썩여 있느냐
# 아니면 도무 다 제각각인가?
# 같은 알파벳이 한번이라도 또 나오면 결과는 no
# 같은 알파벳이 하나라도 없다면 결과는 yes
# 집합(set) 사용하기 - 중복을 허용하지 않습니다.

n = list(input())

num1 = len(n)
num2 = len(set(n))

if num1 == num2:
    print('yes')
else:
    print('no')