# Card Game for Three(ABC Edit)
# aca => 앨리스 A
# accc => 밥 B
# ca => 찰리 C
# 앨리스부터 시작해서 최상단에 a를 뽑음 그럼 앨리스
# 만약 c라면 찰리로 가서 찰리 최상단 뽑기


m1 = list(input())
m2 = list(input())
m3 = list(input())

n = m1.pop(0) #pop은 삭제한 요소를 반환하는 특징이 있다.

while True:
    if n == 'a':
        if len(m1) == 0:
            print('A')
            break
        n = m1.pop(0)
    elif n == 'b':
        if len(m2) == 0:
            print('B')
            break
        n = m2.pop(0)
    else:
        if len(m3) == 0:
            print('C')
            break
        n = m3.pop(0)