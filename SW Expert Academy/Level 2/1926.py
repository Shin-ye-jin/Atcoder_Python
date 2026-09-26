# 1926 간단한 369게임

# 전부다 문자로 입력받고
# 그걸 해체해
# 그걸 전부다 숫자로 치환해서?
# 하나라도 있다면 - or -- 등듣 출력?

n = int(input())

for i in range(1,n+1):
    matrix = list(map(int, str(i)))
    count = 0
    for number in matrix:
        if number % 3 == 0 and number > 0:
            count += 1

    if count == 0:
        print(i,end = ' ')
    else:
        for j in range(count):
            print('-', end = '')
        print(end=' ')