T = int(input())
for t in range(1, T+1):
    arr = list(input())
    print(f'#{t}', end=' ')
    cnt = [13] * 4
    N = len(arr)
    card_lst = []
    for i in range(0, N, 3):
        card_lst.append(''.join(arr[i:i + 3]))
    flag = 1
    for x in range(len(card_lst) - 1):
        for y in range(x + 1, len(card_lst)):
            if card_lst[x] == card_lst[y]:
                flag = 0
                break
    card = ['S', 'D', 'H', 'C']
    for j in range(len(card_lst)):
        for h in range(4):
            if card_lst[j][0] == card[h]:
                cnt[h] -= 1
                break

    if flag:
        print(*cnt)
    else:
        print('ERROR')