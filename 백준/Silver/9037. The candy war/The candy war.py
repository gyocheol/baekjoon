def odd_check():
    for i in range(n):
        if candies[i] % 2:
            candies[i] += 1

def candy_check():
    flag = True
    for candy in candies[1:]:
        if candies[0] != candy:
            flag = False
            break
    return flag

for _ in range(int(input())):
    roof = 0
    n = int(input())
    candies = list(map(int, input().split()))
    if n == 1:
        print(roof)
    else:
        while True:
            odd_check()
            check = candy_check()
            if check:
                break
            roof += 1
            roof_list = [0] * n
            for i in range(n):
                if i == n-1:
                    roof_list[0] += candies[i] // 2
                else:
                    roof_list[i+1] = candies[i]//2
            for i in range(n):
                candies[i] = candies[i]//2 + roof_list[i]
        print(roof)