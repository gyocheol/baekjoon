import math

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):     # 소수는 그 수의 루트만큼만 %를 보면 됨
        if not x % i:
            return False
    return True


while True:
    num = int(input())
    if not num:
        break
    cnt = 0
    for i in range(num+1, num*2+1):
        if isPrime(i):
            cnt += 1
    print(cnt)
