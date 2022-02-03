import math

l = list(map(int, input().split()))
a = math.gcd(l[0],l[1])
b = math.lcm(l[0],l[1])
print(a)
print(b)