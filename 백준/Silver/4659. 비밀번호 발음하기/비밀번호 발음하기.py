import re
while True:
    s = input()
    if s == "end":break
    case1 = len(re.findall("[aeiou]", s)) != 0                  # 모음의 유무 확인
    case2 = len(re.findall("[aeiou]{3}|[^aeiou]{3}", s)) == 0   # 모음 or 자음의 3번 연속 유무 확인
    case3 = len(re.findall("([a-df-np-z])\\1", s)) == 0         # e와 o의 2번 반복 제외 반복 유무 확인

    if case1 and case2 and case3:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
