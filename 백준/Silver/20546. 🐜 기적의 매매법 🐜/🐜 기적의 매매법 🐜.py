seed = int(input())
stocks = [0] + list(map(int, input().split()))
j, s = seed, seed
s_stock, j_stock = [0] * 15, [0] * 15
increase, decrease = 0, 0
for i in range(1, 15):
    j_buy = j // stocks[i]
    if j_buy:
        j_stock[i] = j_buy
        j = j - j_buy * stocks[i]

    if stocks[i-1] < stocks[i]:
        increase += 1
        decrease = 0
    elif stocks[i-1] > stocks[i]:
        decrease += 1
        increase = 0
    else:
        increase, decrease = 0, 0
    s_buy = s // stocks[i]
    if increase >= 3:
        for k in range(i):
            if s_stock[k]:
                s += s_stock[k] * stocks[i]
                s_stock[k] = 0
    elif decrease >= 3:
        s_stock[i] = s_buy
        s -= s_buy * stocks[i]
for i in range(15):
    j += j_stock[i] * stocks[-1]
    s += s_stock[i] * stocks[-1]

if j > s:
    print("BNP")
elif s > j:
    print("TIMING")
else:
    print("SAMESAME")