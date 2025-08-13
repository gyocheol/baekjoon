def solution(board, skill):
    ans = 0
    n = len(board)
    m = len(board[0])
    diff = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    
    # 스킬
    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:
            degree = -degree
        diff[r1][c1] += degree
        diff[r1][c2+1] -= degree    # 우측 누적합 영향 제거
        diff[r2+1][c1] -= degree    # 아래 누적합 영향 제거
        diff[r2+1][c2+1] += degree
    # 가로 누적합
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j-1]
    # 세로 누적합
    for j in range(m):
        for i in range(1, n+1):
            diff[i][j] += diff[i-1][j]
    # board에 적용
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] >= 1:
                ans += 1
        
    return ans