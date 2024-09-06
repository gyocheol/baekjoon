n = int(input())
arr = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and not line[j]:
            line[j] = i+1
            break
        elif not line[j]:
            cnt += 1
print(*line)