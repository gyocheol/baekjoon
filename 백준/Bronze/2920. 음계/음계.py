n = list(map(int, input().split()))

arr = [i for i in range(1, 9)]

if n == arr:
    print('ascending')
elif n == arr[::-1]:
    print('descending')
else:
    print('mixed')