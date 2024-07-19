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
    return gcd(a, b) == 1



