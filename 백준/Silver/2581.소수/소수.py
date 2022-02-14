m = int(input())
n = int(input())
sosu = []

for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        sosu.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                sosu.append(i)
if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))