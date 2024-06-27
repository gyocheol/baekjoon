import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]
first_team = 0
second_team = 0
winner = 1
total = 0
for i in range(n):
    if arr[0][i] == arr[1][i]: # 비길때(첫번 째 경기는 안 비김)
        winner = 1 if winner == 2 else 2
        if winner == 1:
            if second_team < total:
                second_team = total
        else:
            if first_team < total:
                first_team = total
        total = 1
    elif arr[0][i] > arr[1][i]:         # 1번 팀이 2번 팀 보다 수가 클때
        if arr[0][i] - arr[1][i] == 1:  # 1번 팀이 이길 때
            if winner == 1:
                total += 1
            else:
                if second_team < total:
                    second_team = total
                total = 1
                winner = 1
        else:                           # 2번 팀이 이길 때
            if winner == 2:
                total += 1
            else:
                if first_team < total:
                    first_team = total
                total = 1
                winner = 2
    else:                               # 2번 팀이 1번 팀 보다 수가 클때
        if arr[1][i] - arr[0][i] == 1:  # 2번 팀이 이길 때
            if winner == 2:
                total += 1
            else:
                if first_team < total:
                    first_team = total
                total = 1
                winner = 2
        else:                           # 1번 팀이 이길 때
            if winner == 1:
                total += 1
            else:
                if second_team < total:
                    second_team = total
                total = 1
                winner = 1
print(max(first_team, second_team, total))