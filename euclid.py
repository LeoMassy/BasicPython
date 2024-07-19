def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#1であるかどうか
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    """
    | 項目 | 内容 |
    | ---- | ---- |
    | 引数 | 自然数 a, 自然数 b |
    | 処理 | a と b が互いに素か判定する |
    | 返り値 | 判定結果（bool 型） |
    """
    return gcd(a, b) == 1



