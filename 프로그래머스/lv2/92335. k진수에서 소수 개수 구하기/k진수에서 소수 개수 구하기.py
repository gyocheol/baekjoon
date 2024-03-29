def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            # 소수가 아닐떄 False
            return False
    # 1과 자기 자신 빼고 안걸렸을때 True반환
    return True


def solution(n, k):
    answer = 0
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    k_js = base[::-1] + '0'
    total = ''
    for i in range(len(k_js)):
        if k_js[i] == '0':
            if total:
                # 소수이면서 1이 아닐때
                if isPrime(int(total)) and total != '1':
                    answer += 1
                    total = ''
                if total == '1':
                    total = ''
            elif not total:
                pass
        else:
            total += k_js[i]

    return answer