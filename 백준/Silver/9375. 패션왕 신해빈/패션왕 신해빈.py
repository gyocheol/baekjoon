T = int(input())
for _ in range(T):
    N = int(input())
    # 딕셔너리
    weardict = {}
    for i in range(N):
        # 이름과 종류
        name, kind = input().split()
        try: weardict[kind] += 1
        except: weardict[kind] = 1
    cnt = 1
    for k in weardict.values():
        # kind를 안 입는 것 추가 +1
        cnt *= (k+1)
    # 모든 의상을 입지 않는 경우를 제거 -1
    print(cnt-1)