import sys
input = sys.stdin.readline

n = int(input())
ans = 0
armies = [0]*200001

for i in range(n):
    num, state = map(int, input().split())
    if state:
        if armies[num]:
            ans += 1
            armies[num] = 1
        else:
            armies[num] = 1
    else:
        if armies[num]:
            armies[num] = 0
        else:
            ans += 1
print(ans+sum(armies))
