import sys
input = sys.stdin.readline
''' 런타임 에러
n, m = map(int, input().split())
score = list(map(int, input().split()))
ans_dict = {}
for _ in range(m):
    student = list(input().split())
    for i in range(1, n+1):
        if student[i] == "O":
            try: ans_dict[int(student[0])] += score[i-1]
            except: ans_dict[int(student[0])] = score[i-1]
ans = sorted(ans_dict.items(), key=lambda item : (-item[1], item[0]))   # value 내림차순, key 오름차순
print(*ans[0])
'''

n, m = map(int, input().split())
score = list(map(int, input().split()))
ans_dict = {}
for _ in range(m):
    student = list(input().split())
    ans_dict[int(student[0])] = 0
    for i in range(1, n+1):
        if student[i] == "O":
            ans_dict[int(student[0])] += score[i-1]
ans = sorted(ans_dict.items(), key=lambda item : (-item[1], item[0]))   # value 내림차순, key 오름차순
print(*ans[0])
