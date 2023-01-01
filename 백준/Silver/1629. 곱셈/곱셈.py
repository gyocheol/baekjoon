'''
# 분배 법칙, 지수 법칙
지수법칙
A^m+n = A^m * A^n

나머지 분배 법칙
(A*B)%C = (A%C) * (B%C) % C

A^B%C
= ((10 ^ 5) % 12 * (10 ^ 5) % 12 * 10) % 12
= ((10 ^ 2) % 12 * (10 ^ 2) % 12 * 10) % 12 * ((10 ^ 2) % 12 * (10 ^ 2) % 12 * 10) % 12
'''


import sys
input = sys.stdin.readline


def multi(a, b, c):
    if b == 1:
        return a % c
    else:
        # num 순서 : 11, 5, 2, 1, 2(else에서 진행), 5(if에서 진행 후 리턴)
        num = multi(a, b//2, c)
        if b % 2:
            return (num * num * a) % c
        else:
            return (num * num) % c


A, B, C = map(int, input().split())
print(multi(A, B, C))
