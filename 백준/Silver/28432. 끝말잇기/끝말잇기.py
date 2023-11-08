n = int(input())
S = [input() for _ in range(n)]
m = int(input())
A = [input() for _ in range(m)]
if n != 1:
    idx = S.index("?")
    ex_M = []
    if not idx:
        for a in A:
            if a[-1] == S[idx + 1][0]:
                ex_M.append(a)
    elif idx == n-1:
        for a in A:
            if a[0] == S[idx - 1][-1]:
                ex_M.append(a)
    else:
        for a in A:
            if a[0] == S[idx - 1][-1] and a[-1] == S[idx + 1][0]:
                ex_M.append(a)

    for ans in ex_M:
        if ans not in S:
            print(ans)
else:
    print(*A)