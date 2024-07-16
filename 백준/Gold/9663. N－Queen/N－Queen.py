def solve(r):
    if r == n: return 1
    res = 0
    for c in range(n):
        if table[c] or add_table[r+c] or sub_table[r-c]:
            continue
        table[c] = True
        add_table[r+c] = True
        sub_table[r-c] = True

        res += solve(r+1)

        table[c] = False
        add_table[r+c] = False
        sub_table[r-c] = False
    return res


n = int(input())
table = [False] * n
add_table = [False] * (n*2)
sub_table = [False] * (n*2)

print(solve(0))
