# 3x7처럼 숫자x숫자 형태의 3글자 문자열이 들어온다. 가운데 x를 제외한 앞뒤 숫자를 곱한 값을 뱉어낸다.

def multiply_string(s):
    num1 = int(s[0])
    num2 = int(s[2])
    return num1 * num2

S = input() # 3x7 입력
print(multiply_string(S))