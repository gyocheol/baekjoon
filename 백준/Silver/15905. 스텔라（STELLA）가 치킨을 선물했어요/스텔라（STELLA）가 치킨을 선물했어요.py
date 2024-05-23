t = int(input())
score = [list(map(int, input().split())) for _ in range(t)]
ans = 0
if t != 5:
    score.sort(key=lambda x:(-x[0], x[1]))    # 맞힌 문제 수 내림차순, 패널티 오름차순 정렬
    test = score[4][0]
    for i in range(5, t):
        if test == score[i][0]:
            ans += 1
        else:
            break
print(ans)