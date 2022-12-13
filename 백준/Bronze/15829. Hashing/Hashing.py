alphabet = 'abcdefghijklmnopqrstuvwxyz'

N = int(input())
s = input()
ans = 0
for i in range(N):
    x = alphabet.index(s[i])
    ans += (x+1)*(31**i)
print(ans % 1234567891)