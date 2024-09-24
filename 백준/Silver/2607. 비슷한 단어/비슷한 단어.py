n = int(input())
first_word = input()
w_l = len(first_word)
ans = 0
for _ in range(n-1):
    word = input()
    l = len(word)
    visited1 = [True]*w_l
    visited2 = [True]*l
    total = 0
    for i in range(w_l):
        for j in range(l):
            if first_word[i] == word[j] and visited1[i] and visited2[j]:
                visited1[i] = False
                visited2[j] = False
                total += 1
                break
    if w_l - l == 1:    # 첫 단어가 하나 더 많을 때
        if total == l:
            ans += 1
    elif w_l - l == -1: # 첫 단어가 하나 더 적을 때
        if total == w_l:
            ans += 1
    elif w_l == l:      # 같을 때
        if total >= w_l-1:
            ans += 1
print(ans)

