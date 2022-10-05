import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(math.factorial(M)//(math.factorial(N)*math.factorial(M-N)))