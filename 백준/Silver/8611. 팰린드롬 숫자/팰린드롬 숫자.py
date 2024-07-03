import sys
input = sys.stdin.readline

n = int(input())
ans = []
for i in range(2, 11):
    decimal = n
    palindrome = ""
    while decimal:
        remainder = decimal % i
        palindrome = str(remainder) + palindrome
        decimal //= i
    if palindrome == palindrome[::-1]:
        ans.append([i, palindrome])
if ans:
    for i in range(len(ans)):
        print(*ans[i])
else:
    print("NIE")
