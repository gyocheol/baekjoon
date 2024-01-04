# chr(num) : 코드를 문자로
# ord(str) : 문자를 코드로
# print(ord("A")) # 65
# print(ord("a")) # 97

n = int(input())
arr = sorted(list(map(int, input().split())))
secret = sorted(input())
plain = []

for i in range(n):
    if arr[i] == 0:
        plain.append(" ")
    elif arr[i] < 27:
        plain.append(chr(arr[i] + 64))
    else:
        plain.append(chr(arr[i] + 70))

print("y" if plain == secret else "n")