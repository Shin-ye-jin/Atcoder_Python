# 현재 온도 X를 받아서 30도 이상이면 에어컨을 켜야 하므로 “Yes”, 아니면 “No”를 리턴하는 함수이다.

def need_air(temp):
    if temp >= 30:
       return "Yes"
    else:
       return "No"

x = int(input()) # 25 입력
print(need_air(x))
