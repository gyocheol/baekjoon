txt = list(input())
result = []
ask = 97
for i in range(26):
    if chr(ask) in txt:
        result.append(str(txt.index(chr(ask))))
    else:
        result.append(str(-1))
    ask+=1
print(' '.join(result))