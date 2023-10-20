import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d = {}
    flag = False
    word, ans = input(), "OK"
    for i in range(len(word)):
        # word[i+1]로 체크 한 것을 넘어가기 위해
        if flag:
            flag = False
            continue
        # 딕셔너리에 추가
        try:d[word[i]] += 1
        except:d[word[i]] = 1
        
        # 3번째 중복된 알파벳이 왔을 때
        if d[word[i]] == 3:
            if i == len(word)-1 or word[i] != word[i+1]:
                ans = "FAKE"
                break
            flag = True
            d[word[i]] = 0
    print(ans)