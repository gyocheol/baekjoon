n = int(input())

full_time = 60*48       # 48분을 초로 환산
total_list = [0] * full_time
score = [0, 0]
ans = [0, 0]

for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(":"))
    total_list[m*60+s] = team
for s in range(full_time):
    if total_list[s] == '1':
        score[0] += 1
    elif total_list[s] == '2':      # else로 처리하면 0일 때도 2팀이 올라가서 elif 처리
        score[1] += 1
    if score[0] > score[1]:
        ans[0] += 1
    elif score[0] < score[1]:
        ans[1] += 1
for i in range(2):
    print(f'{ans[i]//60:02}:{ans[i]%60:02}')
