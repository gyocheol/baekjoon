import sys
input = sys.stdin.readline

def trimmed():      # 절사평균
    return '{:.2f}'.format(sum(num) / len(num) + 0.00000001)

def adjusted():      # 보정평균
    return '{:.2f}'.format((sum(num) + (num[0]*k) + (num[-1]*k))/n + 0.00000001)


n, k = map(int, input().split())
nums = sorted(float(input()) for _ in range(n))
if k > 0:
    num = nums[k:-k]
    print(trimmed())
    print(adjusted())
else:
    print('{:.2f}'.format(sum(nums)/n + 0.00000001, 2))
    print('{:.2f}'.format(sum(nums)/n + 0.00000001, 2))
