kg = int(input())
cnt = 0
for i in range(1667):
    if cnt == 1:
        break
    for j in range(1001):
        if 3 * i + 5 * j == kg:
            cnt = 1
            print(i + j)
            break
if cnt == 0:
    print(-1)