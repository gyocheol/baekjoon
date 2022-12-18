from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    Q = deque()
    Q.append((n, ''))
    visited[n] = True

    while Q:
        x, order = Q.popleft()
        if x == B:
            print(order)
            break
        else:
            # D
            D = (x*2) % 10000
            if not visited[D]:
                order2 = order + 'D'
                Q.append((D, order2))
                visited[D] = True
                if D == B:
                    print(order2)
                    break
            # S
            S = x - 1 if x != 0 else 9999
            if not visited[S]:
                order2 = order + 'S'
                Q.append((S, order2))
                visited[x] = True
                if S == B:
                    print(order2)
                    break

            s_x = str(x)
            if len(s_x) > 3:
                L = int(s_x[1:] + s_x[0])

                if not visited[L]:
                    order2 = order + 'L'
                    Q.append((L, order2))
                    visited[L] = True
                    if L == B:
                        print(order2)
                        break
            else:
                L = int(s_x + '0')
                if not visited[L]:
                    order2 = order + 'L'
                    Q.append((L, order2))
                    visited[L] = True
                    if L == B:
                        print(order2)
                        break

            xx = '0'*(4-len(s_x)) + s_x
            R = int(xx[-1] + xx[:-1])
            if not visited[R]:
                order2 = order + 'R'
                Q.append((R, order2))
                visited[R] = True
                if R == B:
                    print(order2)
                    break


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    bfs(A)

