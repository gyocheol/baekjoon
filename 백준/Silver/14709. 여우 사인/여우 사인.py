n = int(input())
visited = [0]*4
for _ in range(n):
    sign = list(map(int, input().split()))
    sign.sort()
    if sign == [1, 3]:
        visited[0] = 1
    elif sign == [1, 4]:
        visited[1] = 1
    elif sign == [3, 4]:
        visited[2] = 1
    if 2 not in sign and 5 not in sign: # 여우 손 동작과 일치할 때 visited[3]에 저장 
        visited[3] += 1

if visited == [1, 1, 1, n]:    # 여우일 때
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:                           # 여우가 아닐때
    print("Woof-meow-tweet-squeek")
