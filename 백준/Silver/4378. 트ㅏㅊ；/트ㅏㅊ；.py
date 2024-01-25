import sys
keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    words = sys.stdin.readline().rstrip()
    if words:
        for word in words:
            if word != " ":
                print(keyboard[keyboard.index(word)-1], end="")
            else:
                print(" ", end="")
        print()
    else:
        break