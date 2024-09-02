n, k = map(int, input().split())
binary = [0, 1]
idx = 2
while len(binary) < n*5:
    i = idx
    total = []
    while True:
        if i <= 1:
            if i == 1:
                total.append(i)
            idx += 1
            for i in range(len(total)-1, -1, -1):
                binary.append(total[i])
            break
        b = i % 2
        i //= 2
        total.append(b)
ans = []
for i in range(k-1, len(binary), n):
    ans.append(binary[i])
print(*ans[:5])
