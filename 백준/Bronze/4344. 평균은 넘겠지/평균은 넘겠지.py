import sys

num = int(sys.stdin.readline())

for i in range(num):
    score = list(map(int, input().split()))
    only_score = score[1:]
    over_mean = 0
    mean_score = sum(only_score) / score[0]

    for i in only_score:
        if i > mean_score:
            over_mean += 1
    result = ('{:.3f}'.format(over_mean / score[0] * 100))
    print(str(result) + "%")