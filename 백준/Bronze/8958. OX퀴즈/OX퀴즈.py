n = int(input())

for i in range(n):
    l = str(input())
    s = 0
    score = 0
    for j in l:
        if j == 'O':
            s += 1
            score += s
        else:
            s = 0
    print(score)