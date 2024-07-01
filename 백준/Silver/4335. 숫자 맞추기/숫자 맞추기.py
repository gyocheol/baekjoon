# import sys
# sys.stdin = open("4335.txt")

high, low = [], []
flag = True

while True:
    ollie = int(input())
    if ollie == 0:
        break
    stan = input()
    if stan == "too high":
        high.append(ollie)
    elif stan == "too low":
        low.append(ollie)
    else:
        for h in high:
            if h < ollie or h == ollie:
                flag = False
                break
        if flag:
            for w in low:
                if w > ollie or w == ollie:
                    flag = False
                    break
        if flag:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        high, low = [], []
        flag = True
