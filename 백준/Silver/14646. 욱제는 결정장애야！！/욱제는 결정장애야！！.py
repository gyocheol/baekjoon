import sys
input = sys.stdin.readline
''' 느림
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
'''

n = int(input())
nums = list(input().split())
check = set()
total = 0
ans = 0
for num in nums:
    if num not in check:
        check.add(num)
        total += 1
    else:
        check.remove(num)
        total -= 1
    ans = max(ans, total)
print(ans)