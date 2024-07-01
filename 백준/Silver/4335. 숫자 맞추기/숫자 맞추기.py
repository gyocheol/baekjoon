import sys
input = sys.stdin.readline

high, low = [], []
flag = True
while True:
    ollie = int(input())
    if ollie == 0:
        break
    stan = input().strip()
    if stan == "too high":
        high.append(ollie)
    elif stan == "too low":
        low.append(ollie)
    else:
        if high:
            if min(high) <= ollie:
                flag = False
        if low:
            if max(low) >= ollie:
                flag = False
        if flag:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        high, low = [], []
        flag = True
