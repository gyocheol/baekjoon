N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    flag = 1
    for i in range(len(word)-1):
        if word[i+1] != word[i]:
            new_word = word[i+1:]
            if new_word.count(word[i]):
                flag = 0
                break
    if flag:
        cnt += 1

print(cnt)