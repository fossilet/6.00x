def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    #if n in (5, 8, 24):
    #    return True
    #if n < 5:
    #    return False
    #else:
    #    if n % 5 == 0:
    #        return numPens(n - 5)
    #    if n % 8 == 0:
    #        return numPens(n - 8)
    #    if n % 24 == 0:
    #        return numPens(n - 24)

    for a in range(0, n / 5 + 1):
        for b in range(0, n / 8 + 1):
            for c in range(0 , n / 24 + 1):
                if 5 * a + 8 * b + 24 * c == n:
                    return True
    return False
