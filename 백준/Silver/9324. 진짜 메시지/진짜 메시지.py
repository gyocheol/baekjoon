for _ in range(int(input())):
    d = {}
    flag = False
    word, ans = input(), "OK"
    for i in range(len(word)):
        if flag:
            flag = False
            continue
        try:d[word[i]] += 1
        except:d[word[i]] = 1

        if d[word[i]] == 3:
            if i == len(word)-1 or word[i] != word[i+1]:
                ans = "FAKE"
                break
            flag = True
            d[word[i]] = 0
    print(ans)