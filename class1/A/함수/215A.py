# 문자열 S가 입력. 이 문자가 정확히 “Hello, World!”와 똑같은지 검사하여 맞으면 AC, 틀리면 WA를 출력

def judge_string(string):
    if string == "Hello, World!":
       return "AC"
    else:
       return 'WA'

S = input()
# Hello, World! 입력
print(judge_string(S))
