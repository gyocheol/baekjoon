n = list(map(int, input().split()))
sum_arr = 0
for i in n:
    sum_arr += i ** 2

print(sum_arr % 10)