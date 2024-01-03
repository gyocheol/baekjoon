from math import sqrt

for _ in range(int(input())):
    letter = input()
    n = int(sqrt(len(letter)))
    idx = n
    result = ""
    while idx:
        for i in range(idx-1, len(letter), n):
            result += letter[i]
        idx -= 1
    print(result)