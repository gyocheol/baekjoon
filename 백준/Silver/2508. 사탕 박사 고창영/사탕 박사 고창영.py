import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ans = 0
    input()
    n, m = map(int, input().split())
    box = [input() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if box[i][j] == ">" and j+2 < m:
                if "".join(box[i][j:j+3]) == ">o<":
                    ans += 1
            elif box[i][j] == "v" and i+2 < n:
                if box[i+1][j] == "o" and box[i+2][j] == "^":
                    ans += 1
    print(ans)