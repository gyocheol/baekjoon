A = int(input())
T = int(input())
aid = int(input())

beondegi = []
beon, degi, turn = 1, 1, 1

while True:
    # 번, 데기, 번, 데기
    for _ in range(2):
        beondegi.append((beon, 0))
        beon += 1
        beondegi.append((degi, 1))
        degi += 1
    # turn 에 따른 번 추가
    for _ in range(turn + 1):
        beondegi.append((beon, 0))
        beon += 1
    # turn 에 따른 데기 추가
    for _ in range(turn + 1):
        beondegi.append((degi, 1))
        degi += 1
    turn += 1
    if T <= beon:
        print(beondegi.index((T, aid)) % A)
        break
