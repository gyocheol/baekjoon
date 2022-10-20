N, M = map(int, input().split())     # N : 도감 수록, M : 맞춰야하는 개수
p = {}
for i in range(1, N+1):
    p[input()] = str(i)
p_r = {v:k for k,v in p.items()}
for _ in range(M):
    x = input()
    try: print(p[x])
    except: print(p_r[x])