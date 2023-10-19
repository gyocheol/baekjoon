seed = int(input())
stocks = [0] + list(map(int, input().split()))
j, s = seed, seed
s_stock, j_stock = 0, 0
increase, decrease = 0, 0
for i in range(1, 15):
    # 준현 매수
    if j:
        j_stock += j // stocks[i]
        j = j % stocks[i]
    # 성민
    if stocks[i-1] < stocks[i]:
        increase += 1
        decrease = 0
    elif stocks[i-1] > stocks[i]:
        decrease += 1
        increase = 0
    else:
        increase, decrease = 0, 0
    # 매도
    if increase == 3:
        if s_stock:
            s += s_stock * stocks[i]
            s_stock = 0
    # 매수
    elif decrease >= 3:
        s_stock += s // stocks[i]
        s = s % stocks[i]
# 매도
j += j_stock * stocks[-1]
s += s_stock * stocks[-1]

if j > s:
    print("BNP")
elif s > j:
    print("TIMING")
else:
    print("SAMESAME")
