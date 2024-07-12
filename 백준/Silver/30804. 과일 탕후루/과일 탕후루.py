''' 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
fruit = input().split()

ans = 0
for i in range(n-1):
    if n - 1 - i < ans:
        break
    for j in range(n, i, -1):
        if abs(i-j) > ans:
            if len(set(fruit[i:j])) <= 2:
                ans = len(fruit[i:j])
print(ans)
'''
# 재귀
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
fruit = [0] * 10

def tanghulu(start, end, max_num, kind):
    if end >= n:
        return max_num
    fruit[s[end]] += 1
    if fruit[s[end]] == 1:
        kind += 1
    if kind > 2:
        fruit[s[start]] -= 1
        if not fruit[s[start]]:
            kind -= 1
        start += 1
    max_num = max(max_num, end-start+1)
    return tanghulu(start, end+1, max_num, kind)

print(tanghulu(0, 0, 0, 0))
