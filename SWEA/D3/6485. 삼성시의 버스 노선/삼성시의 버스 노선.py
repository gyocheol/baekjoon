T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t}', end=' ')

    # 노선 저장
    bus = []
    for i in range(N):
        a, b = map(int, input().split())
        # bus.append([j for j in range(a, b+1)])
        for j in range(a, b+1):
            bus.append(j)

    # 노선을 카운트 및 딕셔너리로 저장
    bus_dict = {}
    for i in bus:
        try: bus_dict[i] += 1
        except: bus_dict[i] = 1
    key = list(bus_dict.keys())
    # val = list(bus_dict.values())

    # 정류장
    P = int(input())         # 개수
    bus_stop = [int(input()) for _ in range(P)]     # 정류장 번호
    cnt = [0] * P       # 정답 count

    for i in range(P):
        if bus_stop[i] in key:
            cnt[i] = bus_dict[bus_stop[i]]

    print(*cnt)