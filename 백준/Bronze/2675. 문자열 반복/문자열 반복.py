n = int(input())

for i in range(n):
    num, s = input().split()
    for j in range(len(s)):
        print(s[j]*int(num), end='')
    print()