n, a, b = map(int, input().split())
subjects = [list(map(int, input().split())) for _ in range(10)]
if a >= 66 and b >= 130:
    print("Nice")
else:
    for i in range(8-n):
        sub = subjects[i]
        credit = 6 - sub[0]
        a += sub[0] * 3
        b += (min(credit, sub[1]) + sub[0]) * 3
    if a >= 66 and b >= 130:
        print("Nice")
    else:
        print("Nae ga wae")
