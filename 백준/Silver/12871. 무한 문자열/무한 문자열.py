s = input()
t = input()

# 두 문자열의 길이를 맞추기
fs, ft = s * len(t), t * len(s)

print(0 if ft != fs else 1)
