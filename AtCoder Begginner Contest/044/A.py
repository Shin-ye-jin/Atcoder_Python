# Tak and Hotels (ABC Edit)
n = int(input())
k = int(input())
x = int(input())
y = int(input())

# X 1박당 엔화, 처음으로 K 밤
# Y 하룻밤에 엔, (K+1)-그날 밤과 그 후 밤들
# 10000 * 3 + 9000*(n-k)=2 => 48000
# 10000 * 2 = 20000

if n<k:
    print(n*x)
else:
    print(k*x + (n-k)*y)