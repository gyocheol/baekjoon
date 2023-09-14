def is_possible():
    x_list = board.split(".")
    for i in x_list:
        if len(i) % 2:
            return False
    return True

board = input()

if not is_possible():
    print(-1)
else:
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")
    print(board)