def check_1():  # 행렬의 원소는 1부터 `n*n`(n의 제곱) 범위의 정수로 구성하며, 중복되는 수가 없이 모두 달라야 한다.
    for i in range(n):
        for j in range(n):
            if not check_list[square[i][j]]:
                check_list[square[i][j]] += 1
            else:
                return False
    return True
def check_2():  # 행의 합, 열의 합, 2개의 대각선의 수열의 합은 모두 같다.
    check = (n*(n**2+1)) // 2
    left = 0
    right = 0
    for i in range(n):
        left += square[0+i][0+i]
        right += square[0+i][n-1-i]
    for i in range(n):
        if sum(square[i]) != check:
            return False
        if sum(row[i] for row in square) != check:
            return False

    if left == right == check:
        return True
    return False


n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
check_list = [0]* 10001
if check_1():
    if check_2():
        print("TRUE")
    else:
        print("FALSE")
else:
    print("FALSE")
