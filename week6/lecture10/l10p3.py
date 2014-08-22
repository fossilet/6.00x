def isPrime(n):
    if type(n) != int:
        raise TypeError
    if n <= 0:
        raise ValueError
    if n == 2:
        return True
    for d in range(2, int(n**0.5) + 2):
        if n % d == 0:
            return False
    return True
