# 물건 가격 N에 8% 소비세를 곱한 값 (int(N*1.08))이 정가인 206원보다 작으면 Yay!, 같으면 so-so, 크면 :( 을 출력한다.

N = int(input()) # N은 200
price = int(N*1.08)

if price < 206:
    print("Yay!")
elif price == 206:
    print("so-so")
else:
    print(":(")
