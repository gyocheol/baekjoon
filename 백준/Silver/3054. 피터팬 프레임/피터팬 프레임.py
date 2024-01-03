word = input()
result = [".", ".", "#", ".", "."]

for i, w in enumerate(word, 1):
    frame = "#"
    if not i % 3:
        frame = "*"
        result[2] = result[2][:-1] + frame
    result[0] += f".{frame}.."
    result[1] += f"{frame}.{frame}."
    result[2] += f".{w}.{frame}"
    result[3] += f"{frame}.{frame}."
    result[4] += f".{frame}.."

for i in result:
    print(i)