import sys
input = sys.stdin.readline

for _ in range(int(input())):
    day = 1
    food = int(input())
    pigs = list(map(int, input().split()))
    odd = pigs[0] + pigs[2] + pigs[4]
    even = pigs[1] + pigs[3] + pigs[5]
    while True:
        odd = pigs[0] + pigs[2] + pigs[4]
        even = pigs[1] + pigs[3] + pigs[5]
        total = 0
        if day == 1:
            if sum(pigs) > food:
                print(day)
                break
        else:
            total += pigs[0] + pigs[2] + pigs[4] + (even * 3) + pigs[1] + pigs[3] + pigs[5] + (odd * 3)
            for i in range(6):
                if i % 2:
                    pigs[i] += odd
                else:
                    pigs[i] += even
            if total > food:
                print(day)
                break
        day += 1
