import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
check_list = []
total = 0
ans = 0
for num in nums:
    if num not in check_list:
        check_list.append(num)
        total += 1
    else:
        total -= 1
    ans = max(ans, total)
print(ans)