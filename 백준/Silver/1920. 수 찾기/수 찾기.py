import sys
input = sys.stdin.readline

N = int(input())
card = set(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

for i in test:
    if i in card:
        print(1)
    else:
        print(0)