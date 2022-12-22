import math
N, M = map(int, input().split())
print(math.factorial(N) // (math.factorial(N-M) * math.factorial(M)))
