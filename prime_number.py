def is_prime(n):
    # 1以下の数は素数ではない
    if n <= 1:
        return False
    # 2と3は素数である
    if n <= 3:
        return True
    # 2または3で割り切れる数は素数ではない
    if n % 2 == 0 or n % 3 == 0:
        return False
    # 5から√nまでの奇数を試す
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

