import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt_list = [0] * 26
    flag = False
    word, ans = input().strip(), "OK"
    for i in range(len(word)):
        # word[i+1]로 체크 한 것을 넘어가기 위해
        if flag:
            flag = False
            continue
        cnt_list[ord(word[i])-65] += 1

        # 3번째 중복된 알파벳이 왔을 때
        if cnt_list[ord(word[i])-65] == 3:
            if i == len(word)-1 or word[i] != word[i+1]:
                ans = "FAKE"
                break
            flag = True
            cnt_list[ord(word[i])-65] = 0
    print(ans)