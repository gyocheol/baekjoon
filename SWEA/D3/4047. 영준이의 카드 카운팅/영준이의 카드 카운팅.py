T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    arr = input()
    # print(arr)
    card_case = [13] * 4
    ans = 0
    # 슬라이싱을 통해 카드를 잘라줌
    card_list = []
    for i in range(0, len(arr), 3):
        card_list.append(arr[i:i+3])
    # print(card_list)
    
    # 딕셔너리로 저장
    card_dict = {}
    for i in card_list:
        try: card_dict[i] += 1
        except: card_dict[i] = 1
    # print(card_dict)

    key = list(card_dict.keys())
    value = list(card_dict.values())
    flag = 1
    for i in range(len(value)):
        if value[i] > 1:
            card_case = 'ERROR'
            break

        else:
            if key[i][0] == "S":
                card_case[0] -= 1
            elif key[i][0] == "D":
                card_case[1] -= 1
            elif key[i][0] == "H":
                card_case[2] -= 1
            elif key[i][0] == "C":
                card_case[3] -= 1

    if card_case == 'ERROR':
        print(card_case)
    else:
        print(*card_case)