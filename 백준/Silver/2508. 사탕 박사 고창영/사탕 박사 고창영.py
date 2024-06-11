import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ans = 0
    input()
    n, m = map(int, input().split())
    box = [input() for _ in range(n)]
    for c in box:
        ans += c.count(">o<")
    for r in list(zip(*box)):
        ans += ''.join(r).count("vo^")
    print(ans)

    # 느림
    '''
    for i in range(n):
        for j in range(m):
            if box[i][j] == ">" and j+2 < m:
                if "".join(box[i][j:j+3]) == ">o<":
                    ans += 1
            elif box[i][j] == "v" and i+2 < n:
                if box[i+1][j] == "o" and box[i+2][j] == "^":
                    ans += 1
    '''