X = int(input())
N = int(input())
ans = 0
for _ in range(N):
    money, num = map(int, input().split())
    ans += money * num
if X == ans:
    print('Yes')
else:
    print('No')