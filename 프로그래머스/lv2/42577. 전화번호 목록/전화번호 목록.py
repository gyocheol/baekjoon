def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        prefix = phone_book[i]
        other = phone_book[i+1]

        if prefix in other and not other.index(prefix):
            return False
    return True