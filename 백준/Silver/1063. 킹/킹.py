king, stone, n = map(str, input().split())
moving = {
    "R":[1, 0], "L":[-1, 0], "B":[0, -1], "T":[0, 1], "RT":[1, 1], "LT":[-1, 1], "RB":[1, -1], "LB":[-1, -1]
}
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
k = [alphabet.index(king[0]), int(king[1])]
s = [alphabet.index(stone[0]), int(stone[1])]
for _ in range(int(n)):
    move = input()
    order_r, order_c = moving[move][0], moving[move][1]
    save_king = [k[0] + order_r, k[1] + order_c]
    if 0 <= save_king[0] < 8 and 1 <= save_king[1] < 9:
        if save_king[0] == s[0] and save_king[1] == s[1]:
            save_stone = [s[0] + order_r, s[1] + order_c]
            if 0 <= save_stone[0] < 8 and 1 <= save_stone[1] < 9:
                k = [save_king[0], save_king[1]]
                s = [save_stone[0], save_stone[1]]
        else:
            k = [save_king[0], save_king[1]]
print(f'{alphabet[k[0]]}{str(k[1])}')
print(f'{alphabet[s[0]]}{str(s[1])}')