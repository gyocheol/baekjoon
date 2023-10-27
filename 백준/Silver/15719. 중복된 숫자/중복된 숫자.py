''' 메모리 초과
n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    if arr.count(i) > 1:
        print(i)
'''

''' python 시간 초과 및 pypy 틀림 - 2자릿수 이상을 1 자리로 읽음 
import sys

n = int(input())
nums = sys.stdin.readline().rstrip()    # max 천만이라 숫자로 받으면 메모리 초과 뜸
sum_all = sum(range(1, n))
total = 0
for num in nums:
    if num.isdigit():
        total += int(num)

print(abs(total-sum_all))
'''
import sys

n = sys.stdin.readline().rstrip()
nums = sys.stdin.readline().rstrip()
sum_all = sum(range(1, int(n)))
total = 0
tmp = ""
for num in nums:
    if num.isdigit():
        tmp += num
    else:
        total += int(tmp)
        tmp = ""
print(abs(total+int(tmp)-sum_all))