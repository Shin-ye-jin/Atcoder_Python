# 070A => 숫자를 입력받고 바꿔서 뒤집었을 때 그 값이랑 같은가?

# N(575)

n = input()

tmp = n[::-1]

if n == tmp:
    print('Yes')
else:
    print('No')