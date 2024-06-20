# 구현
n, m = map(int, input().split())
u, l, r, d = map(int, input().split())
words = [list(input()) for _ in range(n)]
puzzle = []
even = ["#", "."]
odd = [".", "#"]
for i in range(n+u+d):
    total = []
    for j in range(m+l+r):
        if u <= i < n+u:
            if i % 2:   # 홀수
                if l <= j < m+l:
                    total.append(words[i-u][j-l])
                    continue
            else:       # 짝수
                if l <= j < m+l:
                    total.append(words[i-u][j-l])
                    continue
        if i % 2:   # 홀수
            total.append(odd[j%2])
        else:       # 짝수
            total.append(even[j%2])
    puzzle.append(total)
for i in range(n+u+d):
    print("".join(puzzle[i]))
