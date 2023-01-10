import sys
sys.setrecursionlimit(10**9)    # 재귀 깊이 늘리기
input = sys.stdin.readline

nums = []

while True:
    try: nums.append(int(input()))
    except: break

# print(nums)

def postorder(s, e):
    if s > e:
        return
    mid = e + 1
    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break

    postorder(s+1, mid-1)       # 왼쪽 확인
    postorder(mid, e)           # 오른쪽 확인
    print(nums[s])

postorder(0, len(nums)-1)