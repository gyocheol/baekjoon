def solution(n):
    def hanoi(m, s, b, d, ans_list):
        if m == 1:
            ans_list.append([s, d])
        else:
            hanoi(m - 1, s, d, b, ans_list)
            ans_list.append([s, d])
            hanoi(m - 1, b, s, d, ans_list)

    ans = []
    hanoi(n, 1, 2, 3, ans)
    return ans