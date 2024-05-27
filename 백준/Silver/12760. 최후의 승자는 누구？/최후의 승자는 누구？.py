import sys
input = sys.stdin.readline

n, m = map(int, input().split())
total = [0] * n
cards = list()
for i in range(n):
    card = sorted(list(map(int, input().split())), reverse=True)    # 가진 카드 중 가장 큰 수를 제출(내림차순 정렬)
    cards.append(card)
players = list(zip(*cards))             # zip을 통해 2차원 배열의 행과 열을 바꿔줌
for t in range(m):
    max_val = max(players[t])           # 가장 큰 카드의 값을 가져오기
    for i in range(n):
        if players[t][i] == max_val:    # 여러 명이 가장 큰 카드의 값을 가질 수 있음
            total[i] += 1
            
max_score = max(total)
for i in range(n):
    if max_score == total[i]:
        print(i+1, end=" ")