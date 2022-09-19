# 1이 있는 리스트 1개 찾기
def one(a):
    l = []
    for i in range(N):
        for j in range(M):
            if a[i][j] == '1':
                l.append(a[i])
                break
    return l[0]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{t}', end=' ')
    # print(*one(arr))
    one_lst = one(arr)
    # 56개씩 짤라서 one_zero list에 넣기
    one_zero = []
    for i in range(len(one_lst)-1, -1, -1):
        # print(one_lst[i])
        if one_lst[i] == '1':
            one_zero.append(one_lst[i+1-56:i+1])
            break
    # print(one_zero)

    my_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    bin_list = []
    for i in range(0, 56, 7):
        bin_list.append(''.join(one_zero[0][i:i + 7]))

    # 딕셔너리에서 숫자를 매칭
    num_list = []
    for i in bin_list:
        num_list.append(int(my_dict[i]))

    odd = 0
    even = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]

    if (even*3+odd) % 10 == 0:
        print(sum(num_list))
    elif (even*3+odd) % 10 != 0:
        print(0)