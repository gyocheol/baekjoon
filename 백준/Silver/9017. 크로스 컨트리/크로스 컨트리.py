# 6명 이하 점수 x
# 먼저 들어온 사람부터 1++
# 가장 낮은 팀 우승
# 점수가 같다면 5번째 주자가 먼저 들어온 팀 승리
# 팀 점수는 상위 4명의 주자 점수

t = int(input())
for _ in range(t):
    n = int(input())
    cross = list(map(int, input().split()))
    valid_teams = {}
    for i in range(1, 201):
        if cross.count(i) == 6:
            valid_teams[i] = 0
    cross_result = []
    total = [0] * (max(valid_teams)+1)
    five = {}
    score = 1
    for i in range(n):
        team = cross[i]
        if team in valid_teams:
            cross_result.append(team)
            valid_teams[team] += 1
            if valid_teams[team] < 5:
                total[team] += score
            score += 1
            if valid_teams[team] == 5:
                five[team] = i
    ans = 0
    min_val = 10 ** 6
    for i in range(len(total)):
        if total[i]:
            if total[i] < min_val:
                min_val = total[i]
                ans = i
            elif total[i] == min_val and ans:
                if five[i] < five[ans]:
                    ans = i
    print(ans)
