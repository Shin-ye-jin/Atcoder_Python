# 158A => 역은 총 3개가 있으며, 각 역은 A사 아니면 B사가 운영함. A사가 운영하는 역과 B사가 운영하는 역 사이에만 버스가 생김

# ! A와 B가 동시에 존재해야 버스가 생길 수 있다. / AAA, BBB 이외의 경우의 수는 전부다 해당이 됨.

tmp = input()

if tmp == 'AAA' or tmp == 'BBB':
    print('No')
else:
    print('Yes')