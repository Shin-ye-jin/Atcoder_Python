# 연월일 달력
n = int(input())
days = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(n):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    m = int(month)
    d = int(day)
    if m != 0 and (1 <= d <= days[m-1]): # 월 검사를 맨 앞에 배치한다.
        print(f"#{i+1}",end=" ")
        print(year+"/"+ month+"/"+day)
    else:
        print(f"#{i+1} {-1}")