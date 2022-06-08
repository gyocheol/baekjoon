A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    h = (B + C) // 60
    B = (B + C) % 60
    A = A + h
    if A >= 24:
        A = A - 24
    print(A, B)

else:
    B = B + C
    print(A, B)