# 1244 [S/W 문제해결 응용] 2일차 - 최대 상금

# 즉, 숫자가 입력되었으면 자리 교환을 했을 때 가장 큰 숫자는?
# 값을 하나씩 쪼개서 리스트로 만들어서
# 그걸 내림차순 정렬해서 하면 될거 같은데
# 이건... 교환횟수가 없을 때 가능하구나 ㅇㅋ...

# 교환 횟수가 주어졌을 때 고려하기
# 완전탐색만 하면 너무 양이 많으니 이미 거쳐간 결과는 걸러내야 한다.
# 큐나 집합을 써서 이미 나온 숫자는 방문 처리를 해버리면 된다.?

n = int(input())

unique_numbers = set() # 빈 셋 생성

number, count = map(int,input().split())
number_s = list(str(number))

n_len = len(number_s)
for i in range(n_len):
    for j in range(i+1, n_len):
        number_s[i], number_s[j] = number_s[j], number_s[i]
        combined = ''.join(number_s)
        unique_numbers.add(combined)

        number_s[i], number_s[j] = number_s[j], number_s[i]

print(unique_numbers)
max_value = max(int(x) for x in unique_numbers)
print(max_value)

# 교환 횟수 1회일 경우 성공
