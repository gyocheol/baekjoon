def solution(today, terms, privacies):
    ans = []
    t = {terms[i].split()[0]:int(terms[i].split()[1]) for i in range(len(terms))}
    y, m, d = today.split(".")
    # 모든 기간에 대한 날짜를 구하기
    total = {}
    for k, v in t.items():
        yy, mm = int(y), int(m)
        if mm > v:
            mm -= v
        else:
            yy -= v//12
            mm -= v%12
            if mm <= 0:
                yy -= 1
                mm += 12
        total[k] = f"{yy}.{mm:02}.{d}"
    print(total)
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if total[term] >= date:
            ans.append(i+1)
    return ans