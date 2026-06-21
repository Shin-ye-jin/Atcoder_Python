# 정수 N이 주어진다. 2^n이 n^2보다 크면 “Yes”, 그렇지 않으면 “No”를 출력한다.

n = int(input()) # 5 입력
if 2**n > n**2:
    print("Yes")
else:
    print("No")
