from collections import Counter
import sys
input = sys.stdin.readline

def mean():
    total = sum(arr)
    average = total/n
    print(round(average))

def median():
    sort_arr = sorted(arr)
    print(sort_arr[n//2])

def mode():
    c = Counter(arr)
    order = c.most_common()
    max_mode = order[0][1]

    modes = []
    for num in order:
        if num[1] == max_mode:
            modes.append(num[0])
    modes.sort()
    if len(modes) > 1:
        print(modes[1])
    else:
        print(modes[0])

def scope():
    max_v = max(arr)
    min_v = min(arr)
    print(max_v - min_v)


n = int(input())
arr = [int(input()) for _ in range(n)]

mean()
median()
mode()
scope()
