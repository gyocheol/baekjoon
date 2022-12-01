N = int(input())
M = int(input())
S = input()

ans, cnt, i = 0, 0, 0

while i < M-1:
    if S[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1

print(ans)